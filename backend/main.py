from flask import Flask, request, jsonify
from flask_cors import CORS
from src.app import chain
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__)
CORS(app)


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True)

    if not data or "question" not in data:
        return jsonify({"error": "Question is required"}), 400

    user_input = data["question"]

    try:
        ai_response = chain.invoke(user_input)
        return jsonify({"answer": ai_response["result"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    return {"status": "ok"}



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
