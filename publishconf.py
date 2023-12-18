# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "YTLin"
RELATIVE_URLS = False

# Parse content and save as JSON for searching
PLUGINS += [
    # 'tipue_search',
    'pelican-ga-pageview',
    'sitemap',
    'share_post'
]
PLUGINS = list(set(PLUGINS))


FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""

# Google Page View Plugin setting
# Reference: https://github.com/jhshi/pelican.plugins.ga_page_view
GOOGLE_SERVICE_ACCOUNT = 'eric-s-blog@erics-blog-408106.iam.gserviceaccount.com'
GOOGLE_KEY_FILE = './erics-blog-408106-476fb2b79b78.json'
GA_START_DATE = '2023-12-01'
GA_END_DATE = 'today'
GA_METRIC = 'ga:pageviews'
POPULAR_POST_START = 'A month ago'
# GOOGLE_ANALYTICS = ""