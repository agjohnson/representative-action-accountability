# -*- coding: utf-8 -*-

extensions = []

project = u'Representative Action Accountability'
slug = u'rep-action-accountability'
copyright = u'2017, Anthony Johnson'
author = u'Anthony Johnson'
language = None
version = u'1.0'
release = u'1.0'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
templates_path = ['_templates']
master_doc = 'index'

pygments_style = 'sphinx'
todo_include_todos = False

html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = '{0}-doc'.format(slug)

latex_elements = {}

latex_documents = [
    (master_doc, '{0}.tex'.format(slug), project, u'Anthony Johnson', 'manual'),
]

man_pages = [
    (master_doc, slug, project, [author], 1)
]

texinfo_documents = [
    (master_doc, slug, project, author, slug, project, 'Miscellaneous'),
]
