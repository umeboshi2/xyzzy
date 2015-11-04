# -*- coding: utf-8 -*-

"""
Created on 2015-10-27
:author: Joseph Rawson (joseph.rawson.works@gmail.com)
"""

from pyramid.view import view_config
from pyramid.view import view_defaults

from xyzzy import _
from xyzzy.resources import CustomContent, MarkDownDocument
from xyzzy.fanstatic import css_and_js
from xyzzy.views import BaseView

from kotti.resources import Content
from kotti_dashboard.fanstatic import eidolon
from kotti_compass.fanstatic import mystyles


# this is the default home view
def main_view(context, request):
    mystyles['bootstrap-custom']['cornsilk'].need()
    eidolon.need()
    return {}


# we need to have a view registered to handle
# the MarkDownDocument context
@view_defaults(context=MarkDownDocument, permission='view')
class MarkdownView(BaseView):
    @view_config(name='view', permission='view',
                 renderer='xyzzy:templates/markdownview.mako')
    def default_view(self):
        return {}
    

@view_defaults(context=CustomContent, permission='view')
class CustomContentViews(BaseView):
    """ Views for :class:`xyzzy.resources.CustomContent` """

    @view_config(name='view', permission='view',
                 renderer='xyzzy:templates/custom-content-default.pt')
    def default_view(self):
        """ Default view for :class:`xyzzy.resources.CustomContent`

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        return {
            'foo': _(u'bar'),
        }

    @view_config(name='alternative-view', permission='view',
                 renderer='xyzzy:templates/custom-content-alternative.pt')
    def alternative_view(self):
        """ Alternative view for :class:`xyzzy.resources.CustomContent`.
        This view requires the JS / CSS resources defined in
        :mod:`xyzzy.fanstatic`.

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        css_and_js.need()

        return {
            'foo': _(u'bar'),
        }


