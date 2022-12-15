from scrapy import cmdline
from pymongo import MongoClient


# cmdline.execute("scrapy runspider imdb/spiders/crawl_films.py -O films.csv".split())
# cmdline.execute("scrapy runspider imdb/spiders/crawl_series.py -O series.csv".split())








############################################################################################
############################################################################################
##                                                                                        ##
##                                       Question 1                                       ##
##                                                                                        ##
############################################################################################
############################################################################################


Q1 = films.find().sort("duration",-1).limit(1)
for i in Q1:
    print(i)
