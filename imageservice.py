from flask import Flask, jsonify, send_file
import os

app = Flask(__name__)

IMAGE_FOLDER = 'static/images'
images = os.listdir(IMAGE_FOLDER)

@app.route('/image/<int:index>', methods=['GET'])
def get_image(index):
    if not images:
        return jsonify({'error': 'No images found'}), 404
    # Get the correct image based on modulo
    image_name = images[index % len(images)]
    image_path = os.path.join(IMAGE_FOLDER, image_name)

    # Return the image path (or send the file itself)
    return send_file(image_path)

if __name__ == '__main__':
    app.run(port=5001)  # Runs the server on localhost:5001
