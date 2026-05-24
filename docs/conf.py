"""Sphinx configuration for barmi.github.io."""

from datetime import datetime

project = "barmi"
author = "barmi"
copyright = f"{datetime.now().year}, {author}"
release = "0.1.0"

language = "ko"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxext.opengraph",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "linkify",
    "substitution",
    "attrs_inline",
]
myst_heading_anchors = 3

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_title = "barmi"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_baseurl = "https://barmi.github.io/"

html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "source_repository": "https://github.com/barmi/barmi.github.io/",
    "source_branch": "main",
    "source_directory": "docs/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/barmi",
            "class": "fa-brands fa-github",
            "html": "",
        },
    ],
}

ogp_site_url = "https://barmi.github.io/"
ogp_site_name = "barmi"
