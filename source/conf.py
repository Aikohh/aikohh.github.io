# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Aikoh's Waker Guide"
copyright = ' 2023, Sega'
author = 'Aikoh'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinxcontrib.youtube', 'sphinxcontrib.video', 'sphinx_git']
# MyST documentation: https://myst-parser.readthedocs.io/en/latest/

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
# Furo theme documentation: https://pradyunsg.me/furo/
html_static_path = ['_static']
html_title = 'Waker Guide'
html_favicon = '_static/UINGSClassWa.ico'

html_theme_options = {
#    "announcement": "<em>Important</em> announcement!",
    "source_repository": "https://github.com/Aikohh/aikohh.github.io",
    "source_branch": "main",
    "source_directory": "source/",
}
