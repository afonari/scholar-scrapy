from scrapy import Spider
from scrapy.selector import Selector
from gscholar.items import GscholarItem


class GscholarSpider(Spider):
    name = "gscholar"
    allowed_domains = ["scholar.google.com"]
    start_urls = [
        "https://scholar.google.com/citations?user=Zmwh_JAAAAAJ&hl=en",
    ]

    def parse(self, response):
        names = Selector(response).xpath('//div[@id="gsc_prf_in"]')

        for n in names:
            name = GscholarItem()
            name['name'] = n.xpath('//div[@id="gsc_prf_in"]/text()').extract()[0]
            yield name