# -*- coding: utf-8 -*-

import os
import sys

DJANGO_PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))
sys.path.append(DJANGO_PROJECT_PATH)

os.environ['DJANGO_SETTINGS_MODULE'] = 'scholar_scrapy.settings'
