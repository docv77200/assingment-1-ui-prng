import os  # To check file existence and handle file operations
import json  # To load JSON data from the image_data.json file
import time  # To introduce a polling interval

def load_image_data():
    """
    Load the image data from the static JSON file.
    """
    with open('static/image_data.json', 'r') as f:
        return json.load(f)

def image_service():
    """
    Image service that listens for random numbers in the text file and maps them to image paths.
    """
    image_file = "imageservice.txt"

    while True:
        if os.path.exists(image_file):
            with open(image_file, "r") as f:
                content = f.read().strip()

            if content.isdigit():  # Check if the content is a valid number
                random_number = int(content)
                image_data = load_image_data()

                # Get the corresponding image path relative to static
                image_path = image_data["images"].get(str(random_number), "/static/images/default.jpg")
                print(f"Image Service: Returned image path {image_path}")

                # Overwrite the file with the relative image path
                with open(image_file, "w") as f:
                    f.write(image_path)

        time.sleep(0.1)  # Reduce polling interval

if __name__ == "__main__":
    image_service()
