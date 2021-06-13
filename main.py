#!/usr/bin/env python3

import youtube_dl
from youtube_search import YoutubeSearch
from audiobook_dl import *

print_banner()

search()

download()

#ydl_opts = {}
#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#    ydl.download(['https://www.youtube.com/watch?v=oy2zDJPIgwc'])
#

# # returns a json string
# 
# ########################################
# 
# results = YoutubeSearch('search terms', max_results=10).to_dict()
# 
# print(results)
# # returns a dictionary
