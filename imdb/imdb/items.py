# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem_films(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    year = scrapy.Field()
    Duration = scrapy.Field()
    note = scrapy.Field()
    n_total = scrapy.Field()
    Genre = scrapy.Field()
    Descriptions = scrapy.Field()
    Director = scrapy.Field()
    Acteurs = scrapy.Field()
    Public = scrapy.Field()
    Pays = scrapy.Field()
    languages = scrapy.Field()
    Metacritic = scrapy.Field()
    senario = scrapy.Field()
    popularity = scrapy.Field()
    avis = scrapy.Field()
    like = scrapy.Field()
    
class ImdbItem_series(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    year = scrapy.Field()
    note = scrapy.Field()
    n_total = scrapy.Field()
    Genre = scrapy.Field()
    Descriptions = scrapy.Field()
    Director = scrapy.Field()
    Acteurs = scrapy.Field()
    Public = scrapy.Field()
    Pays = scrapy.Field()
    languages = scrapy.Field()
    # Metacritic = scrapy.Field()
    senario = scrapy.Field()
    popularity = scrapy.Field()
    avis = scrapy.Field()
    like = scrapy.Field()
    type = scrapy.Field()
    # Duration = scrapy.Field()
    
 