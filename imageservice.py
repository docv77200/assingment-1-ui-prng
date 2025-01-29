import os
import time

def image_service():
    file_path = "imageservice.txt"
    prng_file_path = "prng_service.txt"
    image_folder = "images"  # Folder where images are stored

    # Load all image file paths
    image_files = [file for file in os.listdir(image_folder) if file.lower().endswith((".jpg", ".png", ".jpeg"))]
    num_images = len(image_files)

    if num_images == 0:
        raise RuntimeError("No images found in the 'images' folder.")

    while True:
        # Check if PRNG file exists and has input
        if os.path.exists(prng_file_path):
            with open(prng_file_path, "r") as file:
                data = file.read().strip()

            if data.startswith("run"):
                parts = data.split()
                if len(parts) == 2 and parts[1].isdigit():
                    index = int(parts[1]) % num_images  # Handle modulo logic
                    selected_image = image_files[index]
                    image_path = os.path.join(image_folder, selected_image)

                    # Write "run <image_path>" back to the file
                    with open(file_path, "w") as file:
                        file.write(f"run {image_path}")

        # Sleep to prevent excessive CPU usage
        time.sleep(0.1)

if __name__ == "__main__":
    image_service()
