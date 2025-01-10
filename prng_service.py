# generating random numbers

from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/prng', methods=['GET'])
def prng():
    random_number = random.randint(0, 4)  # Random number between 0 and 4
    return jsonify({'randomNumber': random_number})

if __name__ == "__main__":
    app.run(port=5001, debug=True)  # Runs on a different port
