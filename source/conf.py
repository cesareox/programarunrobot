# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('.') + '/_extensions')

# -- Project information -----------------------------------------------------

project = 'Programar un Robot (con OpenRoberta)'
copyright = '2024'
author = 'www.cesareox.com'
release = '2024'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_design',
    'sphinxcontrib.youtube',
    'sphinxcontrib.manpage',
    'sphinxcontrib.gtagjs',
    'notfound.extension']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
language = 'es'
exclude_patterns = []

html_theme = 'furo'
html_static_path = ['_static']
html_copy_source = False
html_show_copyright = False
html_last_updated_fmt = '- %d %b %Y -'

html_logo = "_static/imags/logo_programarunrobot.webp"
html_favicon = "_static/imags/logo_programarunrobot.webp" 

html_theme_options = {
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    "footer_icons": [
        {
            "name": "CGR",
            "url": "https://www.cesareox.com/",
            "html": """CGR <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
              <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
              <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                </svg>
            """,
            "class": "",
        },
    ],
}


#. Para configurar la página 404

notfound_urls_prefix = ""    

# Pendiente publicar y asignar Google Analytics

#gtagjs_ids = [
#    '',
#]
