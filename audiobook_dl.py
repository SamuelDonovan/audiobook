# audiobook_dl.py>

import youtube_dl
from youtube_search import YoutubeSearch
import os

version=0.1

## Functions
def print_banner():
	os.system('clear')
	print("---------------------------------------")
	print("--------- Audio Book Maker ------------")
	print("----------------------------- v", version ," --\n\n")
	return;

def search():
	results_json = YoutubeSearch('search terms', max_results=1).to_json()
	results_dict = YoutubeSearch('search terms', max_results=1).to_dict()
    
	print(results_json)
	print("\n\n")
	print(results_dict)
	print("\n\n")
	return;

def download():

	ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

	with ydl:
	    result = ydl.extract_info(
	        'https://www.youtube.com/watch?v=oy2zDJPIgwc',
	        download=False # We just want to extract the info
	    )
	
	if 'entries' in result:
	    # Can be a playlist or a list of videos
	    video = result['entries'][0]
	else:
	    # Just a video
	    video = result
	
	print(video)
	video_url = video['url']
	print(video_url)
		
