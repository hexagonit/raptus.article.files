from Acquisition import aq_inner
from zope import interface, component

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize

from raptus.article.core import RaptusArticleMessageFactory as _
from raptus.article.core import interfaces
from raptus.article.files.interfaces import IFiles

class IAttachments(interface.Interface):
    """ Marker interface for the attachments viewlet
    """

class Component(object):
    """ Component which lists attachments of an article
    """
    interface.implements(interfaces.IComponent)
    component.adapts(interfaces.IArticle)
    
    title = _(u'Attachments')
    description = _(u'List of files contained in the article.')
    image = '++resource++attachments.gif'
    interface = IAttachments
    viewlet = 'raptus.article.attachments'
    
    def __init__(self, context):
        self.context = context

class Viewlet(ViewletBase):
    """ Viewlet listing the files contained in the article
    """
    index = ViewPageTemplateFile('attachments.pt')

    @property
    @memoize
    def attachments(self):
        plone = component.getMultiAdapter((self.context, self.request), name=u'plone')
        provider = IFiles(self.context)
        manageable = interfaces.IManageable(self.context)
        items = manageable.getList(provider.getFiles())
        for item in items:
            item.update({'title': item['brain'].Title,
                         'description': item['brain'].Description,
                         'url': item['brain'].getURL(),
                         'icon': plone.getIcon(item['obj']).url})
        return items
