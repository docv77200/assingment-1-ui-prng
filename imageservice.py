from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load image data from JSON
with open('image_data.json', 'r') as f:
    image_data = json.load(f)

@app.route('/image/<int:number>', methods=['GET'])
def get_image(number):
    # Fetch URL from JSON or provide a default
    image_url = image_data["images"].get(str(number), "https://example.com/images/default.jpg")
    return jsonify({'imageURL': image_url})

if __name__ == "__main__":
    app.run(port=5002, debug=True)
