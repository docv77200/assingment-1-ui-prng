import os
import json
import time

# Load image data from JSON
def load_image_data():
    with open('static/image_data.json', 'r') as f:
        return json.load(f)

def image_service():
    image_file = "imageservice.txt"
    
    while True:
        if os.path.exists(image_file):
            with open(image_file, "r") as f:
                content = f.read().strip()
            
            if content.isdigit():  # Check if the content is a valid number
                random_number = int(content)
                image_data = load_image_data()
                
                # Get the corresponding image path
                image_path = image_data["images"].get(str(random_number), "static/images/default.jpg")
                print(f"Image Service: Returned image path {image_path}")

                # Overwrite the file with the image path
                with open(image_file, "w") as f:
                    f.write(image_path)
        
        time.sleep(1)  # Prevent busy-waiting

if __name__ == "__main__":
    image_service()
