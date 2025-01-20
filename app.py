from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connection string (use environment variable for security in production)
MONGO_URI = os.getenv("mongodb+srv://Harsha1234:Harsha1234@cluster1.mongodb.net/college_db?retryWrites=true&w=majority")

try:
    client = MongoClient("mongodb+srv://Harsha1234:Harsha1234@cluster1.mongodb.net/college_db?retryWrites=true&w=majority")
    db = client["college_db"]
    college_collection = db["college_details"]
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    client = None

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask App!"

@app.route("/colleges", methods=["GET"])
def get_colleges():
    if client is None:
        return jsonify({"error": "Database connection failed"}), 500
    try:
        colleges = list(college_collection.find({}, {"_id": 0}))
        return jsonify({"colleges": colleges})
    except Exception as e:
        return jsonify({"error": f"Failed to fetch data: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
