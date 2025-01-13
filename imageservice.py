from flask import Flask, jsonify
import os
import json

app = Flask(__name__, static_folder='static')

# Load image data dynamically from the static folder
def load_image_data():
    # Construct the full path to the JSON file in the static folder
    json_path = os.path.join(app.static_folder, 'image_data.json')
    print(f"Looking for JSON file at: {json_path}")  # Debugging path issue
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"JSON file not found at: {json_path}")
    with open(json_path, 'r') as f:
        return json.load(f)

@app.route('/image/<int:number>', methods=['GET'])
def get_image(number):
    try:
        image_data = load_image_data()
        # Fetch the URL from the JSON file or return a default image URL
        image_url = image_data["images"].get(str(number), "https://example.com/images/default.jpg")
        return jsonify({'imageURL': image_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(port=5002, debug=True)
