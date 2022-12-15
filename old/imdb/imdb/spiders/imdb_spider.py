import scrapy

class imdbSpider(scrapy.Spider):
    name = 'imdb_name'
    start_urls = [    
        'https://www.imdb.com/chart/top/'
    ]

    def parse(self, response):
        # title = response.css('title::text')[0].extract()
        # title = response.css('title::text').extract_first()   # extract_first is better than [0]
        title = response.css('h1.header::text').extract()
        subtitle = response.css('div.byline::text').extract()
        title_movie = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "titleColumn", " " ))]//a/text()').extract()
        year_movie = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "secondaryInfo", " " ))]/text()').extract()
        rating  = response.xpath('//strong/text()').extract()
        yield {'titletext' : title, 'subtitle' : subtitle, 'title_movie' : title_movie, 'year_movie' : year_movie, 'rating' : rating}