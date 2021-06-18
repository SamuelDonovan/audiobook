#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from audiobook_dl import *
import os

app = Flask(__name__)
@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        search=request.form["search_form"]
        file_format=request.form["format_form"]
        os.system("rm downloads/download.*")
        url_suffix=search_function(search)
        download_function(url_suffix, file_format)
        #return redirect(url_for("search_page", searched=search))
        file_name='download.' + file_format
        return send_from_directory(directory='./downloads', filename=file_name, as_attachment=True)
        #return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='192.168.1.215', debug=True)
