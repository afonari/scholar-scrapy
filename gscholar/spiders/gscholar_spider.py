# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from gscholar.items import GscholarItem


class GscholarSpider(CrawlSpider):
    name = "gscholar"
    allowed_domains = ["scholar.google.com"]
    start_urls = [
        "https://scholar.google.com/citations?user=Zmwh_JAAAAAJ&hl=en",
    ]

    rules = [
        Rule(LinkExtractor(allow=r'citations\?view_op=list_colleagues'),
         callback='parse_colleagues', follow=True)
    ]

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
            #item['title'] = question.xpath(
            #    'a[@class="question-hyperlink"]/text()').extract()[0]
            items.append(item)
        #
        return items
