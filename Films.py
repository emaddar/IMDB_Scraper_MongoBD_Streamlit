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
def get_youtube_url(query):
    videosSearch = VideosSearch(str(query), limit = 2)
    return videosSearch.result()['result'][0]['link']


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
# col2.header('IMDB Movies')
col2.markdown("<h1 style='text-align: center; color: black;'> IMDB Movies </h1>", unsafe_allow_html=True)
col2.image("https://mediabrief.com/wp-content/uploads/2021/11/IMAGE-IMDb-most-anticipated-Indian-movies-Nov-2021-MEDIABRIEF.png")
st.write("IMDb is an online database of information related to films, television programs, and video games. It is operated by [IMDb.com](https://www.imdb.com/), Inc., a subsidiary of Amazon. The database contains information such as the cast and crew of a particular film or television show, as well as ratings and user reviews. IMDb is a popular resource for people looking for information about movies and television shows.")

st.title('Class Movies')
mygrid0 = make_grid(1,3)
class_by = mygrid0[0][0].selectbox('Class top movie(s) by :',('note', 'year', 'Acteurs', 'Genre', 'duration'))
class_by_limit = mygrid0[0][1].number_input('Limit :',min_value = 1, max_value = 100)
class_sort_by = mygrid0[0][2].selectbox('Sort type :',('Descending', 'Ascending'))

if class_sort_by == 'Descending':
    search_data = films.find().sort(class_by,-1).limit(class_by_limit)
else :
    search_data = films.find().sort(class_by,1).limit(class_by_limit)

mygrid_class = make_grid(class_by_limit,2)
count = 1
for i in search_data :
    
    mygrid_class[count-1][0].markdown(f""" #### {count} : {i['title'][0]}""")
    mygrid_class[count-1][0].markdown(f""" :watch:  {i['duration']} minutes""")
    mygrid_class[count-1][0].markdown(f""" ###### :star:  {i['note']}/10 (NOTE IMDb) """)
    mygrid_class[count-1][0].markdown(f""" :date:  {i['year']}""")
    mygrid_class[count-1][0].markdown(f""" :crossed_flags:  {i['Pays']}""")
    mygrid_class[count-1][0].markdown(f""" :movie_camera:  {i['Genre']}""")
    mygrid_class[count-1][0].markdown(f""" :page_with_curl:  {i['Descriptions'][0:200]}""")


    
    mygrid_class[count-1][1].video(get_youtube_url(i['title'][0]))
    count +=1
    
    

# mygrid1 = make_grid(1,5)
# first_top_250_movies = films.find().sort("Note",-1).limit(5)
# j = 0
# for i in first_top_250_movies :
#     first_top_250_movies = i['title'][0]
#     videosSearch = VideosSearch(str(first_top_250_movies), limit = 2)
#     link_youtube = videosSearch.result()['result'][0]['link']
#     mygrid1[0][j].write(first_top_250_movies)
#     mygrid1[0][j].video(link_youtube)
#     j += 1




