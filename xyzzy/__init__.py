# -*- coding: utf-8 -*-

"""
Created on 2015-10-27
:author: Joseph Rawson (joseph.rawson.works@gmail.com)
"""

from kotti.resources import File
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('xyzzy')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                xyzzy.kotti_configure

        to enable the ``xyzzy`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' xyzzy'
    settings['kotti.alembic_dirs'] += ' xyzzy:alembic'
    settings['kotti.available_types'] += ' xyzzy.resources.MarkDownDocument'
    #settings['kotti.fanstatic.view_needed'] += ' xyzzy.fanstatic.css_and_js'
    File.type_info.addable_to.append('CustomContent')


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('xyzzy:locale')
    config.add_static_view('static-xyzzy', 'xyzzy:static')

    config.add_route('home', '/')
    config.add_view('xyzzy.views.view.main_view',
                    route_name='home',
                    permission='view',
                    renderer='kotti_dashboard:templates/mainview.mako')
    
    config.scan(__name__)
