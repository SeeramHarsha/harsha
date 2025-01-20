from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
# Replace '<username>', '<password>', and '<cluster-url>' with your MongoDB connection details
print("hello")
client = MongoClient("mongodb://localhost:27017/college_db")
db = client["college_db"]
college_collection = db["college_details"]

@app.route("/colleges", methods=["GET"])
def get_colleges():
    # Retrieve all college details from the database
    colleges = list(college_collection.find({}, {"_id": 0}))  # Exclude MongoDB's '_id' field
    return jsonify({"colleges": colleges})

if __name__ == "__main__":
    app.run(debug=True)
