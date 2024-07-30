#!/usr/bin/env python3
"""
setup a basic flask app and create a single route that simply out put
"Welcome to Holberton" as page title and "Hello World" as header
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)