from flask import Flask, jsonify, request, redirect, url_for
from markupsafe import escape
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def incrementer():
    return "Welcome to the KroneAPI"

#For testing displaying input
@app.route('/test/<string:name>/')
def hello(name):
    return f", {escape(name)}"

#Gets the return of the LLM and makes it available to the frontend
@app.route('/article', methods=['GET'])
def receive_article(article):
    '''Assumed JSON structure
    data = {
        title,
        content,
        word_count}'''
    data = json.loads(article)
    return data

#Gets the string input and forwards it to the LLM
#The mehod gets input from a html form (article_input in this case)
@app.route('/input', methods=['POST', 'GET'])
def give_input():
    if request.method == 'POST':
        input = request.form['article_input']
        return redirect(url_for('hello', name = input))
    else:
        input = request.args.get('article_input')
        return redirect(url_for('hello', name = input))


#More error handlers to be added...
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)