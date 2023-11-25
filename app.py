from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId  # Import ObjectId from bson module

app = Flask(__name__)
CORS(app, resources={r"/get_listings": {"origins": "*"}})

# Connect to your MongoDB cluster
client = MongoClient('mongodb+srv://jhaadi4444:work123@work.ooz3uja.mongodb.net/')
db = client['newDb']
collection = db['working']

# Route to fetch data from MongoDB and serve it as JSON
@app.route('/get_listings', methods=['GET'])
def get_listings():
    listings = list(collection.find({}))
    # print(listings)

    # Convert ObjectId to string for serialization
    for item in listings:
        item['_id'] = str(item['_id'])  # Convert ObjectId to string

    return jsonify(listings)

if __name__ == '__main__':
    app.run(debug=True)
