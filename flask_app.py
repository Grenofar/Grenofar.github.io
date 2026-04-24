from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SECRET_CODE = "5120"

@app.route("/check")
def check():
    code = request.args.get("code")

    if code == SECRET_CODE:
        return jsonify({
            "ok": True,
            "link": "https://github.com/grenofar"
        })

    return jsonify({
        "ok": False
    })