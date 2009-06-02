sc.pfg.brazilianfields
======================

Overview
--------

sc.pfg.brazilianfields is a product that aims to provide Brazil-specific fields 
for use with PloneFormGen


Requirements
------------

    - Products.PloneFormGen >= 1.5 (http://plone.org/products/ploneformgen)
    
Installation
------------
    
To enable this product,on a buildout based installation:

    1. Edit your buildout.cfg and add ``sc.pfg.brazilianfields``
       to the list of eggs to install ::

        [buildout]
        ...
        eggs = 
            ...
            sc.pfg.brazilianfields

    2. Tell the plone.recipe.zope2instance recipe to install a ZCML slug::

        [instance]
        ...
        zcml = 
            ...
            sc.pfg.brazilianfields

If another package depends on the sc.pfg.brazilianfields egg or 
includes its zcml directly you do not need to specify anything in the 
buildout configuration: buildout will detect this automatically.

After updating the configuration you need to run the ''bin/buildout'',
which will take care of updating your system.

Go to the 'Site Setup' page in the Plone interface and click on the
'Add/Remove Products' link.

Choose the product (check its checkbox) and click the 'Install' button.

Uninstall -- This can be done from the same management screen, but only
if you installed it from the quick installer.

Note: You may have to empty your browser cache and save your resource registries
in order to see the effects of the product installation.

Sponsoring
----------

Development of this product was sponsored by `Simples Consultoria 
<http://www.simplesconsultoria.com.br/>`_ customers, including (but not limited 
to):

    * Escola Sao Paulo
    
    * Essencis
    
    * Revista do Brasil


Credits
-------

    * Erico Andrei (erico at simplesconsultoria dot com dot br) - Packaging and
      plumbing.


