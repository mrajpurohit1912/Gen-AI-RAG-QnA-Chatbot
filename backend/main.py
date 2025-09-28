from flask import Flask,request,jsonify
from flask_cors import CORS
from src.app import chain
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__)
CORS(app)
@app.route("/ask",methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data["question"]
    ai_response = chain.invoke(user_input)
    return jsonify({"answer":ai_response["result"]})

if __name__ == "__main__":
    app.run(port=5000,debug=True)



