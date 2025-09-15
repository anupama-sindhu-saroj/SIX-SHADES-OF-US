from flask import Flask, jsonify
from flask_cors import CORS
import json
import os
import time

app = Flask(__name__)
CORS(app)

# Load schedule data from JSON
schedule_file = os.path.join(os.path.dirname(__file__), "schedules", "sample_schedule.json")
with open(schedule_file, "r") as f:
    schedule_data = json.load(f)

# Simulation start time
start_time = time.time()

@app.route("/api/schedule", methods=["GET"])
def get_schedule():
    return jsonify(schedule_data)

@app.route("/api/trains", methods=["GET"])
def get_trains():
    current_time = int(time.time() - start_time)

    trains_status = []
    for train in schedule_data["trains"]:
        # Simple simulation: each train moves from 0 → 1 in 20 seconds
        progress = min(current_time / 20, 1)
        trains_status.append({
            "id": train["id"],
            "route": train["route"],
            "position": round(progress, 2)
        })

    return jsonify(trains_status)

if __name__ == "__main__":
    app.run(debug=True)
