#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from audiobook_dl import *
import os

app = Flask(__name__)
@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        search=request.form["search_form"]
        os.system("rm downloads/download.m4a")
        url_suffix=search_function(search)
        download_function(url_suffix)
        #return redirect(url_for("search_page", searched=search))
        return send_from_directory(directory='./downloads', filename='download.m4a', as_attachment=True)
        #return render_template('index.html')
    else:
        return render_template('index.html')

@app.route("/test")
def search_page(searched):
    return f"<h1>Searching for: {searched} ...</h1>"

if __name__ == "__main__":
    app.run(host='192.168.1.215', debug=True)
