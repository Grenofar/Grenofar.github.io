from flask import Flask, request, jsonify
from router import router
from ai import ask_ai

app = Flask(__name__)

def workflow(user_input):
    action = router(user_input)

    if action == "summarize":
        return ask_ai("Résume : " + user_input)
    elif action == "code":
        return ask_ai("Code : " + user_input)
    else:
        return ask_ai(user_input)

@app.route("/ai")
def ai():
    q = request.args.get("q")
    return jsonify({"response": workflow(q)})