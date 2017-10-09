from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Picture


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
        sites=response.xpath('//img[@r_src]')
        print 'sites',sites
        items = []

        for site in sites:
            item = Picture()
            # item['name'] = site.css(
            #     'a > div.site-title::text').extract_first().strip()
            # print item['name']
            item['url'] = site.xpath('@r_src').extract()
            print item['url']
            item['description'] = site.xpath('@alt').extract()
            if len(item['description']):
                print item['description'][0]
            items.append(item)

        return items
