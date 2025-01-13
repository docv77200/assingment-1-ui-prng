# generating random numbers

from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Define the number of images
IMAGE_COUNT = 6  # Replace with the actual number of images in your dataset

@app.route('/prng', methods=['GET'])
def prng():
    random_number = random.randint(0, 8)  # Generate a number between 0 and 8
    valid_number = random_number % IMAGE_COUNT  # Map to valid image index
    return jsonify({'randomNumber': valid_number})  # Return the valid index

if __name__ == "__main__":
    app.run(port=5001, debug=True)
