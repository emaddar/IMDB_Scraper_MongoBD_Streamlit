# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from dotenv import load_dotenv
load_dotenv()

import pymongo
class Films:

    def __init__(self):
        self.conn = pymongo.MongoClient(
            os.getenv("mylink")
        )

        db= self.conn['IMDB']
        self.collection = db['Films']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item



class Series:

    def __init__(self):
        self.conn = pymongo.MongoClient(
             os.getenv("mylink")
            # 'localhost',
            # 27017
        )

        db= self.conn['IMDB']
        self.collection = db['Series']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
