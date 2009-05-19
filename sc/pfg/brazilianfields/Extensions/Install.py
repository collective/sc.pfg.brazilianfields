from StringIO import StringIO
from Products.CMFCore.utils import getToolByName

def install(self, reinstall=False):
    out = StringIO()
    
    # install dependency: PloneFormGen
    print >> out, "Installing dependency products"
    portal_qi = getToolByName(self, 'portal_quickinstaller')
    if reinstall and portal_qi.isProductInstalled('PloneFormGen'):
        portal_qi.reinstallProducts(['PloneFormGen'])
    elif portal_qi.isProductInstallable('PloneFormGen') and not portal_qi.isProductInstalled('PloneFormGen'):
        portal_qi.installProduct('PloneFormGen')
    
    print >> out, "Installing default sc.pfg.brazilianfields setup profile"
    setup_tool = getToolByName(self, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile(
            'profile-sc.pfg.brazilianfields:default',
            purge_old=False)
    print >> out, "Successfully installed sc.pfg.brazilianfields."
    return out.getvalue()
