from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_event = {"type": None, "timestamp": None, "payload": None}

@app.route("/event", methods=["POST"])
def receive_event():
    global latest_event
    content = request.get_data(as_text=True)
    latest_event = {
        "type": "event",
        "payload": content,
        "timestamp": request.headers.get("Date")
    }
    print(f"✅ Received: {content}")
    return jsonify({"status": "ok"}), 200

@app.route("/latest", methods=["GET"])
def get_latest_event():
    return jsonify(latest_event)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
