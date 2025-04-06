# api.py
from flask import Flask, request, jsonify
from gpt4free import you

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json.get("prompt")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        result = you.Completion.create(prompt=prompt, chat=False)
        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
