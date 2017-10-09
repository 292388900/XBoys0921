from scrapy.item import Item, Field


class Website(Item):
    name = Field()
    description = Field()
    url = Field()

class Picture(Item):
    url =Field()
    name=Field()
    description = Field()
