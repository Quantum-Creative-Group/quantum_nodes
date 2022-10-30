# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys
# Quantum Nodes source code
# Plus, Animation Nodes source code should be next to quantum_nodes/ folder
sys.path.insert(0, os.path.abspath('../../'))
# Filters for spelling
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Quantum Nodes'
copyright = '2021-2022, Quantum-Creative-Group'
author = 'Quantum-Creative-Group'

# The full version, including alpha/beta/rc tags
release = '0.1.2'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinxcontrib.spelling',
    'sphinxemoji.sphinxemoji',
]

# Remove the 'view source code' button on pages
html_show_sourcelink = False

# String specifying a file containing a list of words known to be spelled
# correctly but that do not appear in the language dictionary selected
# by spelling_lang. The file should contain one word per line.
spelling_word_list_filename = 'spelling_wordlist.txt'

# The PyEnchant tokenizer supports a “filtering” API for processing words
# from the input. Filters can alter the stream of words by adding,
# replacing, or dropping values.
from MethodNameFilter import MethodNameFilter
spelling_filters = ['MethodNameFilter.MethodNameFilter']

# Show suggestions
spelling_show_suggestions = True

# TODO: fix this, not working...
# Exclude python files
# spelling_exclude_patterns = ['**/quantum_nodes/*']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
}

# Add a logo
html_logo = '_static/images/logo.png'

# Add favicon
html_favicon = '_static/images/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/developers_manual/ascii_art_file_architecture.css',
    'css/global.css',
]
