def image_service():
    image_file = "image-service.txt"

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
