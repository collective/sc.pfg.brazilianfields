""" Form fields, implemented via Archetypes Fields, Validators and Widgets"""

__author__  = 'Simples Consultoria <products@simplesconsultoria.com.br>'
__docformat__ = 'plaintext'

from Products.Archetypes.public import *

from Products.ATContentTypes.content.base import registerATCT
from Products.CMFCore.permissions import View

from Products.PloneFormGen.content.fieldsBase import *

from sc.pfg.brazilianfields.config import *

from Products.BrFieldsAndWidgets.BrFieldsAndWidgets import BrPhoneField as brphonefield
from Products.BrFieldsAndWidgets.BrFieldsAndWidgets import CEPField as cepfield
from Products.BrFieldsAndWidgets.BrFieldsAndWidgets import CNPJField as cnpjfield
from Products.BrFieldsAndWidgets.BrFieldsAndWidgets import CPFField as cpffield
from Products.BrFieldsAndWidgets.BrFieldsAndWidgets import BrPhoneWidget
from Products.BrFieldsAndWidgets.BrFieldsAndWidgets import CEPWidget
from Products.BrFieldsAndWidgets.BrFieldsAndWidgets import CNPJWidget
from Products.BrFieldsAndWidgets.BrFieldsAndWidgets import CPFWidget

from sc.pfg.brazilianfields import MessageFactory as _

class BrPhoneField(BaseFormField):
    """ Brazilian Phone Number Field """
    
    schema = BaseFieldSchemaStringDefault + Schema(())
    
    def __init__(self, oid, **kwargs):
        """ initialize class """
        
        BaseFormField.__init__(self, oid, **kwargs)
        
        self.fgField = brphonefield('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=BrPhoneWidget(label=_(u'Phone Number'),
                                 description=_(u'Please inform your complete phone number')),
            )
    

registerATCT(BrPhoneField, PROJECTNAME)

class CepField(BaseFormField):
    """ Brazilian CEP Field """
    
    schema = BaseFieldSchemaStringDefault + Schema(())
    
    def __init__(self, oid, **kwargs):
        """ initialize class """
        
        BaseFormField.__init__(self, oid, **kwargs)
        
        self.fgField = cepfield('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=CEPWidget(label=_(u'CEP'),
                             description=_(u'Please inform CEP for this address.')),
            )
        
    

registerATCT(CepField, PROJECTNAME)

class CnpjField(BaseFormField):
    """ Brazilian CNPJ Field """
    
    schema = BaseFieldSchemaStringDefault + Schema(())
    
    def __init__(self, oid, **kwargs):
        """ initialize class """
        
        BaseFormField.__init__(self, oid, **kwargs)
        
        self.fgField = cnpjfield('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=CNPJWidget(label=_(u'CNPJ'),
                                 description=_(u'Please inform CNPJ.')),
            )
        
    

registerATCT(CnpjField, PROJECTNAME)

class CpfField(BaseFormField):
    """ Brazilian CPF Field """
    
    schema = BaseFieldSchemaStringDefault + Schema(())
    
    def __init__(self, oid, **kwargs):
        """ initialize class """
        
        BaseFormField.__init__(self, oid, **kwargs)
        
        # set a preconfigured field as an instance attribute
        self.fgField = cpffield('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=CPFWidget(label=_(u'CPF'),
                                 description=_(u'Please inform CPF.')),
            )
        
        
    

registerATCT(CpfField, PROJECTNAME)