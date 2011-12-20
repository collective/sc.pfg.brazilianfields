# -*- coding:utf-8 -*-
""" Form fields, implemented via Archetypes Fields, Validators and Widgets"""

__author__ = 'Simples Consultoria <products@simplesconsultoria.com.br>'
__docformat__ = 'plaintext'

from Products.Archetypes.public import Schema

from Products.ATContentTypes.content.base import registerATCT
from Products.CMFCore.permissions import View

from Products.PloneFormGen.content.fieldsBase import BaseFormField
from Products.PloneFormGen.content.fieldsBase import \
                                                 BaseFieldSchemaStringDefault

from Products.BrFieldsAndWidgets import BrFieldsAndWidgets

from sc.pfg.brazilianfields.config import PROJECTNAME

from sc.pfg.brazilianfields import MessageFactory as _


class BrPhoneField(BaseFormField):
    """ Brazilian Phone Number Field """

    schema = BaseFieldSchemaStringDefault + Schema(())

    def __init__(self, oid, **kwargs):
        """ initialize class """

        BaseFormField.__init__(self, oid, **kwargs)

        self.fgField = BrFieldsAndWidgets.BrPhoneField('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=BrFieldsAndWidgets.BrPhoneWidget(label=_(u'Phone Number'),
                                 description=_(u'Please inform your complete phone number')),
            )


registerATCT(BrPhoneField, PROJECTNAME)


class CepField(BaseFormField):
    """ Brazilian CEP Field """

    schema = BaseFieldSchemaStringDefault + Schema(())

    def __init__(self, oid, **kwargs):
        """ initialize class """

        BaseFormField.__init__(self, oid, **kwargs)

        self.fgField = BrFieldsAndWidgets.CepField('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=BrFieldsAndWidgets.CEPWidget(label=_(u'CEP'),
                             description=_(u'Please inform CEP for this address.')),
            )


registerATCT(CepField, PROJECTNAME)


class CnpjField(BaseFormField):
    """ Brazilian CNPJ Field """

    schema = BaseFieldSchemaStringDefault + Schema(())

    def __init__(self, oid, **kwargs):
        """ initialize class """

        BaseFormField.__init__(self, oid, **kwargs)

        self.fgField = BrFieldsAndWidgets.CnpjField('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=BrFieldsAndWidgets.CNPJWidget(label=_(u'CNPJ'),
                                 description=_(u'Please inform CNPJ.')),
            )


registerATCT(CnpjField, PROJECTNAME)


class CpfField(BaseFormField):
    """ Brazilian CPF Field """

    schema = BaseFieldSchemaStringDefault + Schema(())

    def __init__(self, oid, **kwargs):
        """ initialize class """

        BaseFormField.__init__(self, oid, **kwargs)

        self.fgField = BrFieldsAndWidgets.CpfField('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=BrFieldsAndWidgets.CPFWidget(label=_(u'CPF'),
                                 description=_(u'Please inform CPF.')),
            )


registerATCT(CpfField, PROJECTNAME)
