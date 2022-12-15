from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('The Shawshank Redemption', limit = 2)

print(videosSearch.result()['result'][0]['link'])