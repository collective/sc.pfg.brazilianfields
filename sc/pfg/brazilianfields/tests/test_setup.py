# -*- coding: utf-8 -*-
import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles

from sc.pfg.brazilianfields.testing import INTEGRATION_TESTING

PROJECTNAME = 'sc.pfg.brazilianfields'

PRODUCT_DEPENDENCIES = ['Products.BrFieldsAndWidgets',
                        'Products.PloneFormGen']

CONTENTTYPES = ['CepField',
                'CpfField',
                'CnpjField',
                'BrPhoneField']


class BaseTestCase(unittest.TestCase):
    """base test case to be used by other tests"""

    layer = INTEGRATION_TESTING

    def setUpUser(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Editor', 'Reviewer'])
        login(self.portal, TEST_USER_NAME)

    def setUp(self):
        portal = self.layer['portal']
        self.portal = portal
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.pp = getattr(self.portal, 'portal_properties')
        self.wt = getattr(self.portal, 'portal_workflow')
        self.st = getattr(self.portal, 'portal_setup')
        self.setUpUser()


class TestInstall(BaseTestCase):
    """ensure product is properly installed"""

    def test_installed(self):
        self.failUnless(self.qi.isProductInstalled(PROJECTNAME),
                        '%s not installed' % PROJECTNAME)

    def test_base_dependencies_installed(self):
        for p in PRODUCT_DEPENDENCIES:
            if p.startswith('Products'):
                p = p[9:]
            self.failUnless(self.qi.isProductInstalled(p),
                            '%s not installed' % p)


class TestConfig(BaseTestCase):
    """ Ensure we have configured this portal """

    def test_disabled_metatypes(self):
        blacklist = self.pp.navtree_properties.metaTypesNotToList
        for mt in CONTENTTYPES:
            self.failUnless(mt in blacklist,
                            '%s still appearing in listings' % mt)

    def test_search_metatypes(self):
        blacklist = self.pp.site_properties.types_not_searched
        for mt in CONTENTTYPES:
            self.failUnless(mt in blacklist,
                            '%s still appearing in search' % mt)


class TestContentCreation(BaseTestCase):
    """ Test content creation """

    def setUp(self):
        BaseTestCase.setUp(self)
        self.portal.invokeFactory('Folder', 'folder')
        self.folder = self.portal['folder']
        self.folder.invokeFactory('FormFolder', 'ff1')
        self.ff1 = self.folder['ff1']

    def testCreateFormFolder(self):
        self.failUnless('ff1' in self.folder.objectIds())

    def testCreateFields(self):
        for f in CONTENTTYPES:
            fname = "%s1" % f
            self.ff1.invokeFactory(f, fname)
            self.failUnless(fname in self.ff1.objectIds())


class TestUninstall(BaseTestCase):
    """ensure product is properly uninstalled"""

    def setUp(self):
        BaseTestCase.setUp(self)
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.failIf(self.qi.isProductInstalled(PROJECTNAME))


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
