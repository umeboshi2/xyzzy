import os

from kotti.populate import populate_users
from .resources import MarkDownDocument

# copied from kotti.populate.populate
from pyramid.i18n import LocalizerRequestMixin
from pyramid.threadlocal import get_current_registry

from kotti import get_settings
from kotti.resources import DBSession
from kotti.resources import Node

from kotti.security import SITE_ACL
from kotti.util import _
from kotti.workflow import get_workflow

def make_markdown_attrs(name, filename, title=None, description=''):
    if title is None:
        title = name.capitalize()
    body = file(filename).read()
    return dict(name=name, title=title, description=description, body=body)


def populate():
    """
    Create the root node (:class:`~kotti.resources.Document`) and the 'about'
    subnode in the nodes tree if there are no nodes yet.
    """
    lrm = LocalizerRequestMixin()
    lrm.registry = get_current_registry()
    lrm.locale_name = get_settings()['pyramid.default_locale_name']
    localizer = lrm.localizer

    if DBSession.query(Node.id).count() == 0:
        pkgdir = os.path.dirname(__file__)
        pagesdir = os.path.join(pkgdir, 'static/pages')
        #import pdb ; pdb.set_trace()
        root_filename = os.path.join(pagesdir, 'index.md')
        root_atts = make_markdown_attrs('', root_filename,
                                        title='Welcome to XYZZY',
                                        description='Home Page')
        root = MarkDownDocument(**root_atts)
        root.__acl__ = SITE_ACL
        DBSession.add(root)
        webatts = make_markdown_attrs('webdesign',
                                      os.path.join(
                                          pagesdir, 'webdesign/index.md'),
                                      title='Web Design',
                                      description='Pages on Web Design')
        root['webdesign'] = MarkDownDocument(**webatts)
        wpages = ['history', 'development', 'stylesheets',
                  'javascript-components']
        for wp in wpages:
            wpfn = os.path.join(pagesdir, 'webdesign/%s.md' % wp)
            wptitle = ' '.join([p.capitalize() for p in wp.split('-')])
            wpatts = make_markdown_attrs(wp, wpfn, title=wptitle)
            root['webdesign'][wp] = MarkDownDocument(**wpatts)
        wf = get_workflow(root)
        if wf is not None:
            DBSession.flush()  # Initializes workflow
            wf.transition_to_state(root, None, u'public')

    populate_users()

