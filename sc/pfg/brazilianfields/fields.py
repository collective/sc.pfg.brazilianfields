""" Form fields, implemented via Archetypes Fields, Validators and Widgets"""

__author__  = 'Simples Consultoria <products@simplesconsultoria.com.br>'
__docformat__ = 'plaintext'

from Products.Archetypes.public import *
from Products.Archetypes.utils import shasattr

from Products.ATContentTypes.content.base import registerATCT
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.configuration import zconf
from Products.TALESField import TALESString, TALESLines
from Products.CMFCore.permissions import View, ModifyPortalContent
from AccessControl import ClassSecurityInfo
from Products.PloneFormGen.content.fieldsBase import *
from sc.pfg.brazilianfields.config import *
from Products.BrFieldsAndWidgets.BrFieldsAndWidgets import *

class BrPhoneField(BaseFormField):
    """ Brazilian Phone Number Field """
    
    schema = BaseFieldSchemaStringDefault + Schema(())
    
    def __init__(self, oid, **kwargs):
        """ initialize class """
        
        BaseFormField.__init__(self, oid, **kwargs)
        
        self.fgField = BrPhoneField('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=BrPhoneWidget(label='Phone Number',
                                 description='Please inform your complete phone number'),
            )
    

registerATCT(BrPhoneField, PROJECTNAME)

class CepField(BaseFormField):
    """ Brazilian CEP Field """
    
    schema = BaseFieldSchemaStringDefault + Schema(())
    
    def __init__(self, oid, **kwargs):
        """ initialize class """
        
        BaseFormField.__init__(self, oid, **kwargs)
        
        self.fgField = CEPField('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=CEPWidget(label='CEP',
                             description='Please inform CEP for this address.'),
            )
        
    

registerATCT(CepField, PROJECTNAME)

class CnpjField(BaseFormField):
    """ Brazilian CNPJ Field """
    
    schema = BaseFieldSchemaStringDefault + Schema(())
    
    def __init__(self, oid, **kwargs):
        """ initialize class """
        
        BaseFormField.__init__(self, oid, **kwargs)
        
        self.fgField = CNPJField('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=CNPJWidget(label='CNPJ',
                                 description='Please inform CNPJ.'),
            )
        
    

registerATCT(CnpjField, PROJECTNAME)

class CpfField(BaseFormField):
    """ Brazilian CPF Field """
    
    schema = BaseFieldSchemaStringDefault + Schema(())
    
    def __init__(self, oid, **kwargs):
        """ initialize class """
        
        BaseFormField.__init__(self, oid, **kwargs)
        
        # set a preconfigured field as an instance attribute
        self.fgField = CPFField('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=CPFWidget(label='CPF',
                                 description='Please inform CPF.'),
            )
        
        
    

registerATCT(CpfField, PROJECTNAME)