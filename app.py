from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get MongoDB username and password from environment variables
username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')
password = quote_plus(password)  # URL-encode your password if needed

# MongoDB connection
mongo_client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.per6r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = mongo_client["Wish"]
collection = db["products"]

# Define routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/products')
def products():
    products = list(collection.find())
    return render_template('products.html', productsobj=products)

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
