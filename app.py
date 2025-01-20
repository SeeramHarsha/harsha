from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb+srv://seeramharsha63:seeramharsha63@cluster0.mongodb.net/college_db?retryWrites=true&w=majority")
db = client["college_db"]
college_collection = db["college_details"]

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask App!"

@app.route("/colleges", methods=["GET"])
def get_colleges():
    # Retrieve all college details from the database
    colleges = list(college_collection.find({}, {"_id": 0}))  # Exclude MongoDB's '_id' field
    return jsonify({"colleges": colleges})

if __name__ == "__main__":
    app.run(debug=True)
