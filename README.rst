========================
sc.pfg.brazilianfields
========================

.. contents:: Table of Contents
   :depth: 2

Overview
--------
A homage to Brazilian bureaucracy, **sc.pfg.brazilianfields** aims to provide 
Brazil-specific fields for use with `PloneFormGen 
<http://plone.org/products/ploneformgen>`_


Requirements
------------

    * Plone 3.3.x / 4.x (http://plone.org/products/plone)
    
    * Products.PloneFormGen >= 1.5 (http://plone.org/products/ploneformgen)
    
Installation
------------

To enable this product, on a buildout based installation:

    1. Edit your buildout.cfg and add ``sc.pfg.brazilianfields``
       to the list of eggs to install ::

        [buildout]
        ...
        eggs = 
            sc.pfg.brazilianfields

.. note:: Since Plone 3.3 is not is necessary to explictly inform 
          plone.recipe.zope2instance recipe to install the ZCML slug

After updating the configuration you need to run the ''bin/buildout'',
which will take care of updating your system.

Using in a Plone Site
----------------------

Activate it
^^^^^^^^^^^^^^^^^^^^

Go to the 'Site Setup' page in the Plone interface and click on the
'Add/Remove Products' link.

Choose the product **PloneFormGen: Brazilian Fields** (check checkbox at its 
left side) and click the 'Activate' button.


Uninstall
-------------

Go to the 'Site Setup' page in the Plone interface and click on the
'Add/Remove Products' link.

Choose the product **PloneFormGen: Brazilian Fields**, which should be under 
*Activated add-ons*, (check checkbox at its left side) and click the 
'Deactivate' button.

.. note:: You may have to empty your browser cache and save your resource 
          registries in order to see the effects of the product installation.

Sponsoring
----------

Development of this product was sponsored by `Simples Consultoria 
<http://www.simplesconsultoria.com.br/>`_ customers, including (but not limited 
to):

    * `Rede Brasil Atual <http://www.redebrasilatual.com.br/>`_
    
    * `Essencis <http://www.essencis.com.br/>`_
    
    * Escola Sao Paulo


Credits
-------

    * Erico Andrei (erico at simplesconsultoria dot com dot br) - Packaging and
      plumbing.


