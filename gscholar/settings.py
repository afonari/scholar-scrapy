# -*- coding: utf-8 -*-

# Scrapy settings for gscholar project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'gscholar'

SPIDER_MODULES = ['gscholar.spiders']
NEWSPIDER_MODULE = 'gscholar.spiders'

DOWNLOAD_DELAY = 5

DEPTH_LIMIT = 2

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gscholar (+http://www.yourdomain.com)'
