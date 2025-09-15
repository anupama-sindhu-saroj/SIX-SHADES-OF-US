from flask import Flask, render_template
from conflict_detection import detect_conflicts, trains

app = Flask(__name__)

@app.route("/")
def dashboard():
    conflicts = detect_conflicts(trains)
    return render_template("dashboard.html", conflicts=conflicts)

if __name__ == "__main__":
    app.run(debug=True)
