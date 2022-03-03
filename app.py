from venv import create
from flask import Flask, render_template
from flask_pymongo import PyMongo
import datetime

app = Flask(__name__)

# setup mongo connection with database
app.config['MONGO_URI'] = "mongodb://localhost:27017/shows_db"
mongo = PyMongo(app)

# connect to collection
tv_shows = mongo.db.tv_shows

# READ


@app.route("/")
def index():
    # find all items in db and save to a variable
    all_shows = list(tv_shows.find())

    return render_template('index.html', data=all_shows)


@app.route("/create")
def create_data():
    post_data = {'name': 'Lucifer',
                 'seasons': 6,
                 'duration': '45 minutes',
                 'year': 2016,
                 'date_added': datetime.datetime.utcnow()
                 }
    tv_shows.insert_one(post_data)
    post_data = {'name': 'Arrow',
                 'seasons': 8,
                 'duration': '45 minutes',
                 'year': 2012,
                 'date_added': datetime.datetime.utcnow()
                 }
    tv_shows.insert_one(post_data)
    all_shows = list(tv_shows.find())
    return render_template('index.html', data=all_shows)


@app.route("/update")
def update_data():
    tv_shows.update_one({'name': 'Lucifer'}, {'$set': {'year': 2014}})
    all_shows = list(tv_shows.find())
    return render_template('index.html', data=all_shows)


@app.route("/delete")
def delete_data():
    tv_shows.delete_one({'name': 'My Life is Murder'})
    all_shows = list(tv_shows.find())
    return render_template('index.html', data=all_shows)


if __name__ == "__main__":
    app.run(debug=True)
