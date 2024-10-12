from flask import Flask, render_template
from pymongo import MongoClient
from urllib.parse import quote_plus

app = Flask(__name__)

# Replace with your actual MongoDB credentials
username = "host"
password = "host"
password = quote_plus(password)  # URL-encode your password if needed

# MongoDB connection
mongo_client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.per6r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = mongo_client["Wish"]
collection = db["products"]

# Uncomment this line if you want to insert mock data once
#mock_data = [
  #    {"name": "Polo t-Shirt", "tag": "new", "price": 13.99, "image_path": "/static/images/polotshirt.jpg"},
 #   {"name": "t-Shirt", "tag": "new", "price": 8.99, "image_path": "/static/images/tshirt.jpg"},
#    {"name": "Shirt", "tag": "new", "price": 23.99, "image_path": "/static/images/shirt.jpg"}]

#collection.insert_many(mock_data)  # Uncomment this to insert data once

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
