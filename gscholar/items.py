# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
import re

class GscholarItem(Item):
    # define the fields for your item here like:

    id = Field()
    name = Field()
    email_domain = Field()
    #
    def set_id_from_url(self, url):
        self['id'] = re.search(r'user=([\w\-]+)', url).group(1)
