# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------
import os
import sys

_prj_root = os.path.dirname(__file__)
_prj_root = os.path.relpath(os.path.join('..', '..', 'lib'), _prj_root)
_prj_root = os.path.abspath(_prj_root)
sys.path.insert(1, _prj_root)


# -- Project information -----------------------------------------------------

project = 'Rule Engine'
copyright = '2018, Spencer McIntyre'
author = 'Spencer McIntyre'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '0.9'


# -- General configuration ---------------------------------------------------
GITHUB_BRANCH = 'master'
GITHUB_REPO = 'zeroSteiner/rule-engine'
add_module_names = False

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

intersphinx_mapping = {'python': ('https://docs.python.org/3.6', None)}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'RuleEnginedoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'RuleEngine.tex', 'Rule Engine Documentation',
     'Spencer McIntyre', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ruleengine', 'Rule Engine Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'RuleEngine', 'Rule Engine Documentation',
     author, 'RuleEngine', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------
intersphinx_mapping = {'python': ('https://docs.python.org/3.6', None)}

def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    file_name = info['module'].replace('.', '/') + '.py'
    return "https://github.com/{0}/blob/{1}/{2}".format(GITHUB_REPO, GITHUB_BRANCH, file_name)