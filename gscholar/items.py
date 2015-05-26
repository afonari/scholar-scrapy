# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.contrib.djangoitem import DjangoItem
from gscholar.models import User, Organization
import re
#
#import os
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

class GscholarItem(DjangoItem):
    pass
    # define the fields for your item here like:
    #django_model = User
    #id = Field()
    #name = Field()
    #email_domain = Field()
    #
    #def set_id_from_url(self, url):
    #    self['id'] = re.search(r'user=([\w\-]+)', url).group(1)

class GscholarOrganization(DjangoItem):
    # define the fields for your item here like:
    #django_model = Organization
    pass