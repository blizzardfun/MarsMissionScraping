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
                #  values returned  mars_dict={"NASA title":news_title,
                #             "NASA news":news_p,
                #             "JPL featured url":featured_image_url,
                #             "Weather":mars_weather,
                #             "Mars facts":html_table,
                #             "Hemisphere urls":hemisphere_image_urls}
    print("after Mongodb")
    print(entry_list)

    return render_template("index.html")


# Route that will trigger scrape functions
@app.route("/scrape")
def go_scrape():
    mongo.db.mars_data.drop()
    collection=mongo.db.mars_data
    mars_dict=scrape()
    
    # Insert into database
    collection.insert_one( {"entry":mars_dict})

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
