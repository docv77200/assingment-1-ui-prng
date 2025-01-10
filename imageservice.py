from flask import Flask, jsonify

app = Flask(__name__)

# Map random numbers to image file paths
image_map = {
    0: 'images/image1.jpg',
    1: 'images/image2.jpg',
    2: 'images/image3.jpg',
    3: 'images/image4.jpg',
    4: 'images/image5.jpg'
}

@app.route('/image/<int:number>', methods=['GET'])
def get_image(number):
    image_path = image_map.get(number, 'images/default.jpg')  # Default image if number is out of range
    return jsonify({'imagePath': f'/static/{image_path}'})

if __name__ == "__main__":
    app.run(port=5002, debug=True)  # Runs on a different port
