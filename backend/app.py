from flask import Flask, request, jsonify
from chatbot_logic import get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
