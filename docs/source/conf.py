# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ShadowFI'
copyright = '2025, Juan David Guerrero Balaguera'
author = 'Juan David Guerrero Balaguera'

release = '1.0.1'
version = '1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'


html_context = {
    'display_github': True,
    'github_user': 'divadnauj-GB',
    'github_repo': 'shadowfi',
    'github_version': 'main',
    'conf_py_path': '/',
}