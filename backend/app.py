from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # allow frontend to call APIs

# Load schedule data from JSON
schedule_file = os.path.join(os.path.dirname(__file__), "schedules", "sample_schedule.json")
with open(schedule_file, "r") as f:
    schedule_data = json.load(f)

@app.route("/api/schedule", methods=["GET"])
def get_schedule():
    return jsonify(schedule_data)

@app.route("/api/trains", methods=["GET"])
def get_trains():
    # for now, return dummy train positions
    trains = [
        {"id": "Train1", "station": "A", "position": 0.2},
        {"id": "Train2", "station": "B", "position": 0.7}
    ]
    return jsonify(trains)

if __name__ == "__main__":
    app.run(debug=True)
