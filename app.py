from funciones import *
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return 'API WEB SCRAPING'

@app.route('/countries')
def countries():
    data = extract_countries()
    return jsonify(data)

@app.route('/countries/<int:id>')
def countriesDetail(id):
    data = extract_countries_detail(id)
    return jsonify(data)
