from zope import interface

class IFiles(interface.Interface):
    """ Provider for files contained in an article
    """
    
    def getFiles():
        """ Returns a list of files (catalog brains)
        """
