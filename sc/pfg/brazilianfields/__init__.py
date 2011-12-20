# -*- coding:utf-8 -*-
from Products.Archetypes.public import process_types, listTypes
from Products.CMFCore import utils

from zope.i18nmessageid import MessageFactory as BaseMessageFactory

from sc.pfg.brazilianfields.config import PROJECTNAME
from sc.pfg.brazilianfields.config import DEFAULT_ADD_CONTENT_PERMISSION

MessageFactory = BaseMessageFactory('sc.pfg.brazilianfields')


def initialize(context):
    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types = content_types,
        permission = DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti = ftis,
        ).initialize(context)
