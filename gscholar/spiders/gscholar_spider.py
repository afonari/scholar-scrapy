# -*- coding: utf-8 -*-
#from scrapy.contrib.linkextractors import LinkExtractor
#from scrapy.contrib.spiders import CrawlSpider, Rule

from scrapy import Spider, Request
from gscholar.items import GscholarItem
import re

class GscholarSpider(Spider):
    name = 'gscholar'
    allowed_domains = ['scholar.google.com']
    start_urls = [
        'https://scholar.google.com/citations?user=Zmwh_JAAAAAJ&hl=en',
    ]

    #rules = [
    #    Rule(LinkExtractor(allow=r'view_op=list_colleagues', process_value='process_value'),
    #        callback='parse_colleagues', follow=True),
    #    #Rule(LinkExtractor(allow=r'citations\?user='),
    #    #    follow=True)
    #]
    #

    def parse(self, response):
        # self.log('SASHA: response url: %s' % response.url)
        if re.search('\/citations\?user=[\w]+&hl=[\w]+$', response.url):
            self.log('SASHA: user_type url: %s' % response.url)
            redirect_url = response.url + '&view_op=list_colleagues'
            yield Request(redirect_url, callback=self.parse)
            return
        #
        elif re.search('&view_op=list_colleagues', response.url):
            self.log('SASHA: colleague_list_type url: %s' % response.url)
            #
            # this def yields Requests for each colleague
            colleagues = self.parse_colleagues(response)

            for colleague in colleagues:
                redirect_url = 'https://scholar.google.com/citations?user=' + colleague['id'] + '&hl=en&view_op=list_colleagues'
                self.log('SASHA: requesting another list_colleague url: %s ' % redirect_url)
                yield Request(redirect_url, callback=self.parse)
    #
    def parse_colleagues(self, response):
        self.log('SASHA: Entered parse_colleagues')
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
            user_url = colleague.xpath(
                'div[@class="gsc_1usr_text"]/h3[@class="gsc_1usr_name"]/a/@href').extract()[0]
            #self.log('SASHA user_url: %s' % user_url)
            item.set_id_from_url(user_url)
            #
            item['email_domain'] = colleague.xpath(
                'div[@class="gsc_1usr_text"]/div[@class="gsc_1usr_emlb"]/text()').extract()[0]
            item['email_domain'] = item['email_domain'].strip().replace("@","")
            #
            items.append(item)
            #print item
            #
        #
        return items
