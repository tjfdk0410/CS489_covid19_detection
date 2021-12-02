from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/detect/', methods=['POST'])
def _get_data():
    print(request.data)
    out = random.choice(["true", "fake"])
    # out = "fake"
    return out

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8123, debug=True)
