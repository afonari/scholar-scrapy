# -*- coding: utf-8 -*-
#from scrapy.contrib.linkextractors import LinkExtractor
#from scrapy.contrib.spiders import CrawlSpider, Rule

from scrapy import Spider, Request
from gscholar.items import GscholarItem
from gscholar.models import User, Organization

import django
django.setup()

import re

class GscholarSpider(Spider):
    name = 'gscholar'
    allowed_domains = ['scholar.google.com']
    start_urls = [
        'https://scholar.google.com/citations?user=zqzNbPIAAAAJ&hl=en',
    ]

    #rules = [
    #    Rule(LinkExtractor(allow=r'view_op=list_colleagues', process_value='process_value'),
    #        callback='parse_colleagues', follow=True),
    #    #Rule(LinkExtractor(allow=r'citations\?user='),
    #    #    follow=True)
    #]
    #

    def parse(self, response):
        self.log('SASHA: response url: %s' % response.url)
        if re.search('\/citations\?user=[\w\-]+&hl=[\w]+$', response.url):
            self.log('SASHA: user_type url: %s' % response.url)
            redirect_url = response.url + '&view_op=list_colleagues'
            yield Request(redirect_url, callback=self.parse)
            return
        #
        r = re.search('\?user=([\w\-]+)&hl=[\w]+&view_op=list_colleagues', response.url)
        if r:
            author = User.objects.get(id=r.group(1))
            self.log('SASHA: colleague_list_type url: %s for user: %s' % (response.url, author)) 
            #
            # this def yields Requests for each colleague
            colleagues = self.parse_colleagues(response)

            for colleague in colleagues:
                #
                org, created = Organization.objects.get_or_create(email_domain=colleague['email_domain'])
                #
                user, created = User.objects.get_or_create(id=colleague['id'], name=colleague['name'],
                    organization=org)
                #user.coauthors.get_or_create(author)
                #
                redirect_url = 'https://scholar.google.com/citations?user=' + colleague['id'] + '&hl=en&view_op=list_colleagues'
                self.log('SASHA: requesting another list_colleague url: %s ' % redirect_url)
                yield Request(redirect_url, callback=self.parse)
    #
#    def parse_user(self, response):
#        name = response.xpath('//div[@class="gsc_prf_in"]/text()').extract()[0]

    #
    def parse_colleagues(self, response):
        self.log('SASHA: Entered parse_colleagues')
        colleagues = response.xpath('//div[@class="gsc_1usr gs_scl"]')
        #
        items = []
        #
        for colleague in colleagues:
            item = dict()
            #
            item['name'] = colleague.xpath(
                'div[@class="gsc_1usr_text"]/h3[@class="gsc_1usr_name"]/a/text()').extract()[0]
            #
            user_url = colleague.xpath(
                'div[@class="gsc_1usr_text"]/h3[@class="gsc_1usr_name"]/a/@href').extract()[0]
            #self.log('SASHA user_url: %s' % user_url)
            item['id'] = re.search(r'user=([\w\-]+)', user_url).group(1)
            #item.set_id_from_url(user_url)
            #
            # some people don't have verified emails
            try:
                item['email_domain'] = colleague.xpath(
                    'div[@class="gsc_1usr_text"]/div[@class="gsc_1usr_emlb"]/text()').extract()[0]
                item['email_domain'] = item['email_domain'].strip().replace("@","")
            #
            except:
                continue
            #
            items.append(item)
            #print item
            #
        #
        return items
