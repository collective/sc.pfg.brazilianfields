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

from Products.BrFieldsAndWidgets.content import BrFieldsAndWidgets

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
            write_permission=View,
            widget=BrFieldsAndWidgets.BrPhoneWidget(label=_(u'label_phone'),
                                 description=_(u'desc_phone')),
            )


registerATCT(BrPhoneField, PROJECTNAME)


class CepField(BaseFormField):
    """ Brazilian CEP Field """

    schema = BaseFieldSchemaStringDefault + Schema(())

    def __init__(self, oid, **kwargs):
        """ initialize class """

        BaseFormField.__init__(self, oid, **kwargs)

        self.fgField = BrFieldsAndWidgets.CEPField('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=BrFieldsAndWidgets.CEPWidget(label=_(u'label_cep'),
                             description=_(u'desc_cep')),
            )


registerATCT(CepField, PROJECTNAME)


class CnpjField(BaseFormField):
    """ Brazilian CNPJ Field """

    schema = BaseFieldSchemaStringDefault + Schema(())

    def __init__(self, oid, **kwargs):
        """ initialize class """

        BaseFormField.__init__(self, oid, **kwargs)

        self.fgField = BrFieldsAndWidgets.CNPJField('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=BrFieldsAndWidgets.CNPJWidget(label=_(u'label_cnpj'),
                                 description=_(u'desc_cnpj')),
            )


registerATCT(CnpjField, PROJECTNAME)


class CpfField(BaseFormField):
    """ Brazilian CPF Field """

    schema = BaseFieldSchemaStringDefault + Schema(())

    def __init__(self, oid, **kwargs):
        """ initialize class """

        BaseFormField.__init__(self, oid, **kwargs)

        self.fgField = BrFieldsAndWidgets.CPFField('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=BrFieldsAndWidgets.CPFWidget(label=_(u'label_cpf'),
                                 description=_(u'desc_cpf')),
            )


registerATCT(CpfField, PROJECTNAME)
