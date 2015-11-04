# -*- coding: utf-8 -*-

"""
Created on 2015-10-27
:author: Joseph Rawson (joseph.rawson.works@gmail.com)
"""

from kotti.interfaces import IDefaultWorkflow
from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode, UnicodeText

from zope.interface import implements

from xyzzy import _

class MarkDownDocument(Content):
    id = Column(Integer(), ForeignKey('contents.id'), primary_key=True)
    body = Column(UnicodeText())
    mime_type = Column(Unicode(30))
    
    type_info = Content.type_info.copy(
        name=u'MarkDownDocument',
        title=u'MarkDownDocument',
        add_view='add_markdown',
        addable_to=[u'Document', u'MarkDownDocument'],
        )

    def __init__(self, body=u'', mime_type='text/markdown', **kwargs):
        super(MarkDownDocument, self).__init__(**kwargs)
        self.body = body
        self.mime_type = mime_type
        
class CustomContent(Content):
    """ A custom content type. """

    implements(IDefaultWorkflow)

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)
    custom_attribute = Column(Unicode(1000))

    type_info = Content.type_info.copy(
        name=u'CustomContent',
        title=_(u'CustomContent'),
        add_view=u'add_custom_content',
        addable_to=[u'Document'],
        selectable_default_views=[
            ("alternative-view", _(u"Alternative view")),
        ],
    )

    def __init__(self, custom_attribute=None, **kwargs):
        """ Constructor

        :param custom_attribute: A very custom attribute
        :type custom_attribute: unicode

        :param **kwargs: Arguments that are passed to the base class(es)
        :type **kwargs: see :class:`kotti.resources.Content`
        """

        super(CustomContent, self).__init__(**kwargs)

        self.custom_attribute = custom_attribute
