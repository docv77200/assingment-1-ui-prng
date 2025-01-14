# UI Service with File-Based Communication and Debugging
from flask import Flask, render_template, jsonify
import os
import time

app = Flask(__name__)

# Helper functions to read and write to text files
def write_to_file(file_name, content):
    try:
        with open(file_name, "w") as f:
            f.write(content)
        print(f"Debug: Successfully wrote '{content}' to {file_name}")
    except Exception as e:
        print(f"Error: Failed to write to {file_name}. Exception: {e}")

def read_from_file(file_name):
    try:
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                content = f.read().strip()
                print(f"Debug: Successfully read '{content}' from {file_name}")
                return content
        print(f"Debug: File {file_name} does not exist.")
    except Exception as e:
        print(f"Error: Failed to read from {file_name}. Exception: {e}")
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    prng_file = "prng_service.txt"  # File used to communicate with PRNG service
    image_file = "imageservice.txt"  # File used to communicate with Image service

    # Step 1: Write "run" to prng_service.txt
    print("UI Service: Writing 'run' to prng_service.txt")
    write_to_file(prng_file, "run")

    # Step 2: Wait for PRNG Service to respond with a timeout
    print("UI Service: Waiting for PRNG Service to respond")
    start_time = time.time()
    while True:
        random_number = read_from_file(prng_file)
        if random_number and random_number.isdigit():
            print(f"UI Service: Received random number {random_number}")
            break
        if time.time() - start_time > 5:  # Timeout after 5 seconds
            print("UI Service: Timeout waiting for PRNG Service")
            return jsonify({'error': 'PRNG Service timed out'}), 500
        time.sleep(0.05)

    # Step 3: Write the random number to imageservice.txt
    print(f"UI Service: Writing random number {random_number} to imageservice.txt")
    write_to_file(image_file, random_number)

    # Step 4: Wait for Image Service to respond with a timeout
    print("UI Service: Waiting for Image Service to respond")
    start_time = time.time()
    while True:
        image_path = read_from_file(image_file)
        if image_path:
            print(f"UI Service: Received image path {image_path}")
            break
        if time.time() - start_time > 5:  # Timeout after 5 seconds
            print("UI Service: Timeout waiting for Image Service")
            return jsonify({'error': 'Image Service timed out'}), 500
        time.sleep(0.05)

    # Return the image path to the frontend
    print(f"UI Service: Returning image path {image_path} to frontend")
    return jsonify({'imagePath': image_path})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
