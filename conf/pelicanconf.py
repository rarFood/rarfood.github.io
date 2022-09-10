#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#Daniel Santiago
from __future__ import unicode_literals

AUTHOR = u'Daniel Santiago'
SITENAME = u'Daniel Santiago-Rodríguez'
SITEURL = ''

PATH = 'content'
DEFAULT_CATEGORY = 'Blog'
TIMEZONE = 'America/Puerto_Rico'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('My Resumé', 'pdfs/DanielSantiago-Resume.pdf'),
         ('ATACKPR', 'http://atackpr.ccom.uprrp.edu/'),
         ('CCOM', 'http://ccom.uprrp.edu'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://pr.linkedin.com/in/daniel-santiago-aaa13057'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGIN_PATHS = ['pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
            'extensions': ['jinja2.ext.i18n'],
            }

THEME='pelican-themes/pelican-bootstrap3'
#BOOTSTRAP_THEME='cosmo'
BOOTSTRAP_NAVBAR_INVERSE=True
CC_LICENSE = "CC-BY-SA"
GITHUB_USER= "rarFood"
OUTPUT_PATH='../'
DISPLAY_PAGES_ON_MENU=False
MENUITEMS=[("Vita","/vita.html")]
STATIC_PATHS = ['images','pdfs']
GOOGLE_ANALYTICS="UA-117060792-1"
