from flask import Flask, jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config ["BASIC_AUTH_USERNAME"] = "RD"
app.config ["BASIC_AUTH_PASSWORD"] = "123"
basic_auth = BasicAuth(app)

HOST = "localhost"
PORT = 8000

@app.route("/test_auth", methods=["GET"])
@basic_auth.required
def test_auth():
    return jsonify({"message": "Authenticated endpoint is working"}), 200

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Test endpoint is working"}), 200

if __name__ == "__main__":
    print(f"serving at {HOST}:{PORT}")
    app.run(host=HOST, port=PORT, debug=True)