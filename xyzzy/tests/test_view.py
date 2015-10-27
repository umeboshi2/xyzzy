# -*- coding: utf-8 -*-

"""
Created on 2015-10-27
:author: Joseph Rawson (joseph.rawson.works@gmail.com)
"""

from pytest import fixture


@fixture
def dummy_content(root):

    from xyzzy.resources import CustomContent

    root['cc'] = cc = CustomContent(
        title=u'My content',
        description=u'My very custom content is custom',
        custom_attribute='Lorem ipsum'
    )

    return cc


def test_view(dummy_content, dummy_request):

    from xyzzy.views.view import CustomContentViews

    views = CustomContentViews(dummy_content, dummy_request)

    default = views.default_view()
    assert 'foo' in default

    alternative = views.alternative_view()
    assert alternative['foo'] == u'bar'
