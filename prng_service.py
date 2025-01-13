# generating random numbers

from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/prng', methods=['GET'])
def prng():
    random_number = random.randint(0, 6)  # Random number between 0 and 8
    return jsonify({'randomNumber': random_number})

if __name__ == "__main__":
    app.run(port=5001, debug=True)  # Runs on a different port
