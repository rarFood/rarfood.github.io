#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Daniel Santiago'
SITENAME = u'Daniel Santiago-Rodríguez'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Puerto_Rico'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://pr.linkedin.com/in/daniel-santiago-aaa13057'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME='../../pelican-themes/pelican-bootstrap3'
#BOOTSTRAP_THEME='cosmo'
BOOTSTRAP_NAVBAR_INVERSE=True
OUTPUT_PATH='../'
PATH='content'
DISPLAY_PAGES_ON_MENU=False 
MENUITEMS=[("Vita","vita.html")]
