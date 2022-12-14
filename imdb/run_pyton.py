from scrapy import cmdline
from pymongo import MongoClient


# cmdline.execute("scrapy runspider imdb/spiders/crawl_films.py -O films.csv".split())
# cmdline.execute("scrapy runspider imdb/spiders/crawl_series.py -O series.csv".split())





# create a MongoClient instance to connect to the database
client = MongoClient('mongodb://localhost:27017/')

# get a reference to the database
db = client['IMDB']

# get a reference to the collection
films = db['Films']


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
