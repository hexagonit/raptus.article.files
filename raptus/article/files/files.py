from zope import interface, component

from Products.CMFCore.utils import getToolByName

from raptus.article.core.interfaces import IArticle
from raptus.article.files.interfaces import IFiles

class Files(object): 
    """ Provider for files contained in an article
    """
    interface.implements(IFiles)
    component.adapts(IArticle)
    
    def __init__(self, context):
        self.context = context
        
    def getFiles(self):
        """ Returns a list of files (catalog brains)
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        return catalog(portal_type='File', path={'query': '/'.join(self.context.getPhysicalPath()),
                                                 'depth': 1}, sort_on='getObjPositionInParent')
