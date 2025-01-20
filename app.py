from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["college_db"]
college_collection = db["college_details"]

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask App!"

@app.route("/colleges", methods=["GET"])
def get_colleges():
    # Retrieve all college details from the database
    colleges = [
  {
    "name": "ABC Engineering College",
    "location": "Hyderabad",
    "courses": ["CSE", "ECE", "Mechanical"]
  },
  {
    "name": "XYZ College of Arts",
    "location": "Chennai",
    "courses": ["History", "Economics", "English"]
  }
]

    return jsonify({"colleges": colleges})

if __name__ == "__main__":
    app.run(debug=True)
