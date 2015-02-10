#!/usr/bin/env python

from random import randint

from flask import Flask, send_from_directory, jsonify


app = Flask(__name__, static_url_path='/static')
value = 0


@app.route('/', methods=['GET'])
def home():
    return send_from_directory('static', 'index.html')

@app.route('/trash_counter', methods=['GET'])
def trash_counter():
    global value
    value += randint(0, 100)
    return jsonify({'value': value})


if __name__ == '__main__':
    app.run(debug=True)
