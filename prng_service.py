import random
import time
import os

def prng_service():
    file_path = "prng_service.txt"
    image_folder = "images"  # Folder containing the images

    while True:
        # Check if the file exists and contains "run"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                command = file.read().strip()

            if command == "run":
                # Count the number of images in the folder
                image_files = [
                    file for file in os.listdir(image_folder)
                    if file.lower().endswith((".jpg", ".png", ".jpeg"))
                ]
                num_images = len(image_files)

                if num_images == 0:
                    raise RuntimeError("No images found in the 'images' folder.")

                # Generate a pseudo-random number within the range of images
                random_number = random.randint(0, 100) % num_images

                # Write the random number back to the file
                with open(file_path, "w") as file:
                    file.write(str(random_number))

        # Sleep to prevent excessive CPU usage
        time.sleep(0.1)

if __name__ == "__main__":
    prng_service()
