# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrapemars import scrape

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():
    entry_list = mongo.db.mars_data.find_one()      #connect/create database

    return render_template("index.html",entry_list=entry_list)


# Route that will trigger scrape functions
@app.route("/scrape")
def go_scrape():
    # scrape the data 
    # if more than 3 errors occur the previous data will be retained and redisplayed
    mars_dict=scrape()
                #   values returned  mars_dict={
                # "nasa_title":news_title,
                # "nasa_news":news_p,
                # "jpl_featured_url":featured_image_url,
                # "weather":mars_weather,
                # "mars_facts":html_table,
                # "hemisphere_urls":hemisphere_image_urls,
                # "error_count":error_count}

    if mars_dict["error_count"] < 4: 
        #use new data if less than 3 errors else retain previous data
        # disguard old data in db
        mongo.db.mars_data.drop()
        collection=mongo.db.mars_data
        # Insert into database
        collection.insert_one( {"entry":mars_dict})
    else:
        print("ERROR LIMIT REACHED previous data retained")
    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
