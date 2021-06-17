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

def search():
	

	# to_search = input('What book would you like to listen to? \n')
	to_search="mozart night music"
	

	print("\n\n")
	# terminal_input = "youtube-dl ytsearch:" + to_search + " -g"
	# os.system(terminal_input)

	# results_json = YoutubeSearch(to_search, max_results=1).to_json()
	results_dict = YoutubeSearch(to_search, max_results=5).to_dict()

	print("Dict is")
	print(results_dict)
	print("\n\n")

	# print("JSON is")
	# print(results_json)
	# print("\n\n")

	print(results_dict[0]["url_suffix"])
	print(results_dict[1]["url_suffix"])

	url_suffix=results_dict[0]["url_suffix"]
	return url_suffix;

def download(url_suffix):
	to_download="youtube-dl https://www.youtube.com" + url_suffix
	os.system(to_download)