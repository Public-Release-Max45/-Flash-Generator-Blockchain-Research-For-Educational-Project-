"""
Blockchain Research Simulation Backend (Educational Only)
"""

from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/status")
def status():
    return jsonify({
        "project": "Blockchain Research Tool",
        "mode": "simulation",
        "active": True,
        "warning": "No real blockchain transactions are performed"
    })


@app.route("/simulate", methods=["POST"])
def simulate():
    return jsonify({
        "result": "Simulation complete",
        "note": "This is a mock response for educational purposes only"
    })


if __name__ == "__main__":
    app.run(debug=True)
