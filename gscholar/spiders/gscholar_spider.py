# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from gscholar.items import GscholarItem
import re

class GscholarSpider(CrawlSpider):
    name = "gscholar"
    allowed_domains = ["scholar.google.com"]
    start_urls = [
        "https://scholar.google.com/citations?user=Zmwh_JAAAAAJ&hl=en",
    ]

    rules = [
        Rule(LinkExtractor(allow=r'view_op=list_colleagues', process_value='process_value'),
            callback='parse_colleagues', follow=True),
        #Rule(LinkExtractor(allow=r'citations\?user='),
        #    follow=True)
    ]

    def process_value(self, value):
        self.log('[SASHA]: Hi, this is an item page! %s' % value)
        if "citations?user=" in value:
            self.log('[SASHA]: Hi, this is an item page! %s' % value)
            return "value" + "&view_op=list_colleagues"
        else:
            return None
    #
    def process_links(self, links):
        for link in links:
            link.url = "%s&view_op=list_colleagues" % link.url
        #
        #print links
        return links
    #

    def parse_x(self, response):
        names = response.xpath('//div[@id="gsc_prf_in"]')

        for n in names:
            name = GscholarItem()
            name['name'] = n.xpath('//div[@id="gsc_prf_in"]/text()').extract()[0]
            yield name
    #
    def parse_colleagues(self, response):

        colleagues = response.xpath('//div[@class="gsc_1usr gs_scl"]')
        #
        items = []
        #
        for colleague in colleagues:
            item = GscholarItem()
            #
            item['name'] = colleague.xpath(
                'div[@class="gsc_1usr_text"]/h3[@class="gsc_1usr_name"]/a/text()').extract()[0]
            #
            item['email_domain'] = colleague.xpath(
                'div[@class="gsc_1usr_text"]/div[@class="gsc_1usr_emlb"]/text()').extract()[0]
            item['email_domain'] = item['email_domain'].strip().replace("@","")
            #

            #item['title'] = question.xpath(
            #    'a[@class="question-hyperlink"]/text()').extract()[0]
            items.append(item)
        #
        return items
