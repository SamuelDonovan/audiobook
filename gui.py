#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        search=request.form["search_form"]
        return redirect(url_for("search_page", searched=search))
    else:
        return render_template('index.html')

@app.route("/<searched>")
def search_page(searched):
    return f"<h1>{searched}</h1>"

if __name__ == "__main__":
    app.run(host='192.168.1.215', debug=True)
