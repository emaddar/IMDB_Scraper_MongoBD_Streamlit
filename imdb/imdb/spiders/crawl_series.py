import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from ast import literal_eval
from ..items import ImdbItem_series


class CrawlSeriesSpider(CrawlSpider):
    name = 'crawl_series'
    allowed_domains = ['imdb.com']
    # start_urls = ['https://www.imdb.com/chart/top/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'imdb.pipelines.Series' : 400
        }
    }

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250', headers={
            'User-Agent': self.user_agent
        })


    le_films_details = LinkExtractor(restrict_xpaths="//td[@class='titleColumn']/a")
    rule_films_details = Rule(le_films_details,
                             callback='parse_item',
                              follow=False)
    rules = (
      rule_films_details  ,
    )

    def parse_item(self, response):
        items = ImdbItem_series()

        items['title'] = response.xpath('//h1/text()').extract()
        items['year'] = response.xpath('//span[@class="sc-8c396aa2-2 itZqyK"]/text()').extract_first()

        items['duration'] = response.xpath('//li[@class="ipc-inline-list__item"]/text()').extract()
        items['type'] = items['duration'][0]

        items['duration'].pop(0) # remove first element
        # Use re.sub() to replace the characters with nothing
        characters_to_remove = [",", "'"]
        items['duration'] = re.sub("[" + "".join(characters_to_remove) + "]", "", str(items['duration']))
        # if 'h' in items['duration'] and 'm' in items['duration']:
        #       characters_to_remove = ["h", "m"]
        #       items['duration'] = re.sub("[" + "".join(characters_to_remove) + "]", "", str(items['duration']))
        #       items['duration'] = re.sub("    ", ",", items['duration'])
        # # if 'h' in items['duration'] :
        # #     items['duration'] = re.sub("h", ",0", items['duration'])
        # # if 'm' in items['duration'] :
        # #     items['duration'][1] = re.sub("m", "", items['duration'])
        # #     items['duration'][0] =0
        # # items['duration'] = literal_eval(items['duration']) #to convert string to list
        # # items['duration'] = int(items['duration'][0] * 60 + items['duration'][1]) # convert to minutes only
        
        


        items['note'] = response.xpath('//span[@class="sc-7ab21ed2-1 jGRxWM"]/text()').extract_first()
        items['n_total'] = response.xpath('//div[@class="sc-7ab21ed2-3 dPVcnq"]/text()').extract_first()
        items['Genre'] = response.xpath('//span[@class="ipc-chip__text"]/text()').extract()[:-1]
        items['Descriptions'] = response.xpath('//span[@class="sc-16ede01-2 gXUyNh"]/text()').extract()
        items['Director'] = response.xpath('//a[@class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"]/text()').extract_first()
        items['Acteurs'] = response.xpath('//a[@class="sc-bfec09a1-1 gfeYgX"]/text()').extract()
        
        items['Public'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]/a/text()').extract()
        

        items['Pays'] = response.xpath("/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section[@class='ipc-page-section ipc-page-section--base celwidget']/div[@class='sc-f65f65be-0 ktSkVi']/ul[@class='ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base']/li[@class='ipc-metadata-list__item'][1]/div[@class='ipc-metadata-list-item__content-container']/ul[@class='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base']/li[@class='ipc-inline-list__item']/a[@class='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link']/text()").extract()
        # items['color'] = response.xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[13]/div[2]/ul/li[4]/div/ul/li/a/text()').extract()
        items['languages'] = response.xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section/div[2]/ul/li[4]/div/ul/li/a/text()').extract()
        items['avis'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/ul/li[1]/a/span/span[1]/text()').extract()
        items['senario'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[2]/div/ul/li[1]/a/text()').extract()
        items['like'] = response.xpath('//a[@class="ipc-poster-card__title ipc-poster-card__title--clamp-2 ipc-poster-card__title--clickable"]/span/text()').extract()
        items['popularity'] = response.xpath('//div[@class="sc-edc76a2-1 gopMqI"]/text()').extract_first()

        yield items
        
        # { 
        #     'popularity' : popularity,
        #     'Pays' : Pays,
        #     'title': title,
        #     'year' : year,
        #     'duration (minutes)' : duration,
        #     'type' : type,
        #     'note' : note,
        #     'n_total' : n_total,
        #     'Genre' : Genre,
        #     'Director' : Director,
        #     'Acteurs' : Acteurs,
        #     'Public' : Public,
        #     'color' : color,
        #     'languages' : languages,
        #     'you may like' : like,
        #     'senario' : senario,
        #     'avis' : avis,
        #     'Descriptions' : Descriptions,
            
        # }
