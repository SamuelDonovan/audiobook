#!/usr/bin/env python3
from youtube_search import YoutubeSearch
from sys import platform
import os
import json

def search_function(to_search):
	results_dict = YoutubeSearch(to_search, max_results=1).to_dict()
	url_suffix=results_dict[0]["url_suffix"]
	return url_suffix;

def download_function(url_suffix, file_format):
	to_download="youtube-dl -f " + file_format + " -o downloads/download." + file_format + " https://www.youtube.com" + url_suffix
	os.system(to_download)