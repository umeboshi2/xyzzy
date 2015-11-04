# -*- coding: utf-8 -*-

"""
Created on 2015-10-27
:author: Joseph Rawson (joseph.rawson.works@gmail.com)
"""

import colander
from kotti.views.edit import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config
from kotti_jsonapi.rest import restify

from xyzzy import _
from xyzzy.resources import CustomContent, MarkDownDocument

class MarkDownSchema(ContentSchema):
    body = colander.SchemaNode(
        colander.String(),
        title='Body',
        missing='',
        )

# this is needed to use kotti_jsonapi
@restify(MarkDownDocument)
def markdown_schema_factory(context, request):
    return MarkDownSchema()

class CustomContentSchema(ContentSchema):
    """ Schema for CustomContent. """

    custom_attribute = colander.SchemaNode(
        colander.String(),
        title=_(u"Custom attribute"))



@view_config(name=CustomContent.type_info.add_view, 
             permission=CustomContent.type_info.add_permission,
             renderer='kotti:templates/edit/node.pt')
class CustomContentAddForm(AddFormView):
    """ Form to add a new instance of CustomContent. """

    schema_factory = CustomContentSchema
    add = CustomContent
    item_type = _(u"CustomContent")


## we need to have views registered for both
# edit and add actions for MarkDownDocument context
    
@view_config(name=MarkDownDocument.type_info.add_view, 
             permission=MarkDownDocument.type_info.add_permission,
             renderer='kotti:templates/edit/node.pt')
class MarkDownAddForm(AddFormView):
    schema_factory = MarkDownSchema
    add = MarkDownDocument
    item_type = 'MarkDownDocument'

@view_config(name='edit',
             permission='edit',
             renderer='kotti:templates/edit/node.pt')
class MarkDownEditForm(AddFormView):
    schema_factory = MarkDownSchema
    


@view_config(name='edit', context=CustomContent, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class CustomContentEditForm(EditFormView):
    """ Form to edit existing CustomContent objects. """

    schema_factory = CustomContentSchema
