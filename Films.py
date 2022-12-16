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

st.sidebar.image("https://beafunmum.com/wp-content/uploads/2017/03/kids-movies-parents-like.jpg")

def add_bg_from_url():
    st.markdown(
         f'''
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/white-background-with-3d-hexagonal-pattern-design_1017-28443.jpg?w=2000");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         ''',
         unsafe_allow_html=True
     )

add_bg_from_url()

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

st.title(':checkered_flag: Sort Movies')
with st.expander("Click here"):
    mygrid0 = make_grid(1,3)
    class_by = mygrid0[0][0].selectbox('Class top movie(s) by :',('note', 'year', 'duration', 'Metacritic', 'popularity', 'avis'))
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
        mygrid_class[count-1][0].markdown(f""" :crossed_flags:  {', '.join(i['Pays'])}""")
        mygrid_class[count-1][0].markdown(f""" :movie_camera:  {', '.join(i['Genre'])}""")
        mygrid_class[count-1][0].markdown(f""" Language(s):  {', '.join(i['languages'])}""")
        mygrid_class[count-1][0].markdown(f""" :page_with_curl:  {i['Descriptions'][0:200]}""")


        
        mygrid_class[count-1][1].video(get_youtube_url(i['title'][0]))
        count +=1
    
    
find_all = films.find()
year_list = []
title_list = []
Genre_list = []
Pays_list = []
languages_list = []
Acteurs_list = []
Director_list = []
for i in find_all:
    year_list.append(i['year'])
    title_list.append(', '.join(i['title']))
    Genre_list.append(i['Genre'])
    Pays_list.append(i['Pays'])
    languages_list.append(i['languages'])
    Acteurs_list.append(i['Acteurs'])
    Director_list.append(i['Director'])
    
    
Genre_list = list(set([item for sublist in Genre_list for item in sublist]))
Pays_list = list(set([item for sublist in Pays_list for item in sublist]))
languages_list = list(set([item for sublist in languages_list for item in sublist]))
Acteurs_list = list(set([item for sublist in Acteurs_list for item in sublist]))


st.title(':clapper: Search Movie')
with st.expander("Click here"):
    mygridSearch = make_grid(1,3)
    search_by = mygridSearch[0][0].selectbox('Search top movie(s) by :',('title', 'year', 'Genre', 'Pays', 'languages', 'Acteurs', 'Director'))
    if search_by == 'title' :
        search_in = mygridSearch[0][1].selectbox(f'Search in {search_by} :',(title_list))
        search_limit = 1
    elif search_by == 'year' :
        search_in = mygridSearch[0][1].selectbox(f'Search in {search_by} :',(year_list))
    elif search_by == 'Genre' :
        search_in = mygridSearch[0][1].selectbox(f'Search in {search_by} :',(Genre_list))
    elif search_by == 'Pays' :
        search_in = mygridSearch[0][1].selectbox(f'Search in {search_by} :',(Pays_list))
    elif search_by == 'languages' :
        search_in = mygridSearch[0][1].selectbox(f'Search in {search_by} :',(languages_list))
    elif search_by == 'Acteurs' :
        search_in = mygridSearch[0][1].selectbox(f'Search in {search_by} :',(Acteurs_list))
    elif search_by == 'Director' :
        search_in = mygridSearch[0][1].selectbox(f'Search in {search_by} :',(Director_list))
    
    if search_by in ['year', 'Genre', 'Pays', 'languages', 'Acteurs', 'Director'] :
        search_limit = mygridSearch[0][2].number_input('Limit :',min_value = 1, max_value = 100, key = 'K1')
    

    # search_data = films.find({f"{search_by}":{"$in":f"{search_by}"}}).limit(search_limit)
    search_data = films.find({f"{search_by}":{"$in":[f"{search_in}"]}}).sort(f"{search_by}",1).limit(search_limit)
    mygrid_search = make_grid(search_limit,2)
    count = 1
    for i in search_data :
        mygrid_search[count-1][0].markdown(f""" #### {i['title'][0]}""")
        mygrid_search[count-1][0].markdown(f""" :watch:  {i['duration']} minutes""")
        mygrid_search[count-1][0].markdown(f""" ###### :star:  {i['note']}/10 (NOTE IMDb) """)
        mygrid_search[count-1][0].markdown(f""" :date:  {i['year']}""")
        mygrid_search[count-1][0].markdown(f""" :crossed_flags:  {', '.join(i['Pays'])}""")
        mygrid_search[count-1][0].markdown(f""" :movie_camera:  {', '.join(i['Genre'])}""")
        mygrid_search[count-1][0].markdown(f""" Language(s):  {', '.join(i['languages'])}""")
        mygrid_search[count-1][0].markdown(f""" :page_with_curl:  {i['Descriptions'][0:200]}""")

        mygrid_search[count-1][1].video(get_youtube_url(i['title'][0]))
        count +=1

        for k in range(7):
            st.write('')

        mygrid_may_like = make_grid(1,3)
        mygrid_may_like[0][1].markdown(""" #### Movies you may like """)

        if search_by == 'title' :
            mygrid_like = make_grid(1,5)
            for j in range(5):
                if i['like'][j]:
                    mygrid_like[0][j].markdown(f""" #####  {i['like'][j]}""")
                    mygrid_like[0][j].video(get_youtube_url(i['like'][j]))
    
    

    
    
