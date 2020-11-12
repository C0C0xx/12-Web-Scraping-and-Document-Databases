from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
@app.route("/")
def index():
    mars = mongo.db.mars_data.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    marsdb = mongo.db.mars_data
    mars_scrape_result = scrape_mars.scrape()
    marsdb.update({}, mars_scrape_result, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)



