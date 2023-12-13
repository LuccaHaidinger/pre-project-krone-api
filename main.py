from flask import Flask, jsonify, abort
from markupsafe import escape
import json

app = Flask(__name__)


@app.route('/')
def incrementer():
    return "Welcome to the KroneAPI"


@app.route('/<string:name>/')
def hello(name):
    if name is None:
        abort(404)

    return f"Hello, {escape(name)}"


@app.route('/article/<article>', methods=['GET'])
def receive_article(article):
    '''Assumed JSON structure
    data = {
        title,
        content,
        word_count}'''
    data = json.loads(article)

    return data


@app.route('/article/input', methods=['POST'])
def give_input(input):
    return input


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


app.run()