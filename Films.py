import streamlit as st
from scrapy import cmdline
from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
from youtubesearchpython import VideosSearch


st.set_page_config(layout="wide")


# cmdline.execute("scrapy runspider imdb/spiders/crawl_films.py -O films.csv".split())
# cmdline.execute("scrapy runspider imdb/spiders/crawl_series.py -O series.csv".split())



# create a MongoClient instance to connect to the database
client = MongoClient(os.getenv("mylink"))

# get a reference to the database
db = client['IMDB']

# get a reference to Films collection
films = db['Films']
# get a reference to Series collection
series = db['Series']



# make any grid with a function
def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid


############################################################################################
############################################################################################
##                                                                                        ##
##                              Generale Informations                                     ##
##                                                                                        ##
############################################################################################
############################################################################################

col1, col2, col3 = st.columns(3)
col2.header('IMDB Movies')
st.write("IMDb is an online database of information related to films, television programs, and video games. It is operated by [IMDb.com](https://www.imdb.com/), Inc., a subsidiary of Amazon. The database contains information such as the cast and crew of a particular film or television show, as well as ratings and user reviews. IMDb is a popular resource for people looking for information about movies and television shows.")

mygrid = make_grid(1,5)

first_top_250_movies = films.find().sort("Note",-1).limit(5)
j = 0
for i in first_top_250_movies :
    first_top_250_movies = i['title'][0]
    videosSearch = VideosSearch(str(first_top_250_movies), limit = 2)
    link_youtube = videosSearch.result()['result'][0]['link']
    mygrid[0][j].write(first_top_250_movies)
    mygrid[0][j].video(link_youtube)
    j += 1




