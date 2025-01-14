# UI Service with File-Based Communication
from flask import Flask, render_template, jsonify
import os
import time

app = Flask(__name__)

# Helper functions to read and write to text files
def write_to_file(file_name, content):
    with open(file_name, "w") as f:
        f.write(content)

def read_from_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return f.read().strip()
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    prng_file = "prng-service.txt"
    image_file = "image-service.txt"

    # Step 1: Write "run" to prng-service.txt
    write_to_file(prng_file, "run")

    # Step 2: Wait for PRNG Service to respond
    while True:
        random_number = read_from_file(prng_file)
        if random_number and random_number.isdigit():
            break
        time.sleep(0.1)  # Reduce polling interval

    # Step 3: Write the random number to image-service.txt
    write_to_file(image_file, random_number)

    # Step 4: Wait for Image Service to respond
    while True:
        image_path = read_from_file(image_file)
        if image_path:
            break
        time.sleep(0.1)  # Reduce polling interval

    # Return the image path to the frontend
    return jsonify({'imagePath': image_path})

if __name__ == "__main__":
    app.run(port=5000, debug=True)