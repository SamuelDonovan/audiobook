#import youtube_dl
from youtube_search import YoutubeSearch
from sys import platform
import os
import json

version=0.1


## Functions
def print_banner():
	if platform == "linux" or platform == "linux2":
		# linux
		os.system('clear')
	elif platform == "darwin":
		# OS X
		os.system('clear')
	elif platform == "win32":
		# Windows...
		os.system('cls')

	print("---------------------------------------")
	print("---------- Audiobook Maker ------------")
	print("----------------------------- v", version ," --\n\n")
	return;

def search_function(to_search):
	results_dict = YoutubeSearch(to_search, max_results=1).to_dict()
	url_suffix=results_dict[0]["url_suffix"]
	return url_suffix;

def download_function(url_suffix):
	to_download="youtube-dl -f m4a -o downloads/download.m4a https://www.youtube.com" + url_suffix
	os.system(to_download)