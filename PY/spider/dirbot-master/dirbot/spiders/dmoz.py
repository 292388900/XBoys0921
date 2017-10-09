from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"

    start_urls = [
        "http://news.baidu.com/"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sites = response.xpath('//a[@href]')
        print "sites",sites
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.xpath('@alt').extract()
            item['url'] = site.xpath('@href').extract()
            # print item['url']

            # item['url'] = site.xpath(
            #     'a/@href').extract_first().strip()
            item['description'] = site.xpath('text()').extract()
            for i in item['description']:
                print i
            items.append(item)

        return items
