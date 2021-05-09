from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
from bson import json_util
from bson.objectid import ObjectId
import json

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")


MONGO_URI = f'mongodb+srv://{USER}:{PASSWORD}@{DB_HOST}/{DB_NAME}?retryWrites=true'
MONGO_DATABASE = f'{DB_NAME}'

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)

@app.route('/news', methods=['GET'])
def get_news():
    print(request.form['tags'])
    news = mongo.db.News.find()
    response = json_util.dumps(news)
    return Response(response, mimetype="application/json")

@app.route('/news/<id>', methods=['GET'])
def get_new(id):
    new = mongo.db.News.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(new)
    return Response(response, mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True)