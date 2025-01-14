import os
import time

def image_service():
    file_path = "imageservice.txt"
    image_folder = "images"  # Folder where images are stored

    # Load all image file paths
    image_files = [file for file in os.listdir(image_folder) if file.lower().endswith((".jpg", ".png", ".jpeg"))]
    num_images = len(image_files)

    if num_images == 0:
        raise RuntimeError("No images found in the 'images' folder.")

    while True:
        # Check if the file exists and has input
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = file.read().strip()

            if data.isdigit():
                index = int(data) % num_images  # Handle modulo logic
                selected_image = image_files[index]
                image_path = os.path.join(image_folder, selected_image)

                # Write the selected image path back to the file
                with open(file_path, "w") as file:
                    file.write(image_path)

        # Sleep to prevent excessive CPU usage
        time.sleep(0.1)

if __name__ == "__main__":
    image_service()
