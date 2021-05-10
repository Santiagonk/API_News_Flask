from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
from bson import json_util
from bson.objectid import ObjectId
import json
from decouple import config as config_decouple

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")


MONGO_URI = f'mongodb+srv://{USER}:{PASSWORD}@{DB_HOST}/{DB_NAME}?retryWrites=true'
MONGO_DATABASE = f'{DB_NAME}'

def create_app():
    app = Flask(__name__)    
    return app

app = create_app()

app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def main():
    return "NEWS API FLASK"

@app.route('/news', methods=['GET'])
def get_all_news():
    query = {}
    offset = 0
    per_page = 400
    try:
        offset = int(request.args['offset'])
    except:
        pass
    try:
        per_page = int(request.args['per_page'])
    except:
        pass
    news = mongo.db.News.find().skip(offset).limit(per_page)
    response = json_util.dumps(news)
    return Response(response, mimetype="application/json")

@app.route('/new', methods=['GET'])
def get_news():
    query = {}
    offset = 0
    per_page = 10
    try:
        offset = int(request.args['offset'])
    except:
        pass
    try:
        per_page = int(request.args['per_page'])
    except:
        pass
    news = mongo.db.News.find(query).skip(offset).limit(per_page)
    response = json_util.dumps(news)
    return Response(response, mimetype="application/json")

@app.route('/new/<id>', methods=['GET'])
def get_new(id):
    new = mongo.db.News.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(new)
    return Response(response, mimetype="application/json")

@app.route('/tag/<tag>', methods=['GET'])
def get_tag(tag):
    query = {}
    offset = 0
    per_page = 10
    try:
        offset = int(request.args['offset'])
    except:
        pass
    try:
        per_page = int(request.args['per_page'])
    except:
        pass
    query['tag'] = { '$in' : [tag]}
    new = mongo.db.News.find(query).skip(offset).limit(per_page)
    response = json_util.dumps(new)
    return Response(response, mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True)