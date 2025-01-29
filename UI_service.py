# Updated UI Service
import os
import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def wait_for_file_update(file_path, keyword, timeout=5):
    start_time = time.time()
    while time.time() - start_time < timeout:  # Wait max 5 seconds
        time.sleep(0.01)  # Faster polling
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read().strip()
                if content.startswith(keyword):
                    return content
    return None  # Timeout case

def run_ui():
    prng_file = "prng_service.txt"
    image_file = "imageservice.txt"

    def handle_button_click():
        # Trigger PRNG Service
        with open(prng_file, "w") as file:
            file.write("run")

        # Wait for PRNG Service to generate a number
        random_number_content = wait_for_file_update(prng_file, "run", timeout=3)
        if random_number_content:
            parts = random_number_content.split()
            if len(parts) == 2 and parts[1].isdigit():
                random_number = int(parts[1])
            else:
                messagebox.showerror("Error", "Invalid response from PRNG Service")
                return
        else:
            messagebox.showerror("Error", "PRNG Service did not respond in time")
            return

        # Pass the random number to Image Service
        with open(image_file, "w") as file:
            file.write(f"run {random_number}")

        # Wait for Image Service to return an image path
        image_path_content = wait_for_file_update(image_file, "run", timeout=5)
        if image_path_content:
            parts = image_path_content.split(maxsplit=1)
            if len(parts) == 2:
                image_path = parts[1]
            else:
                messagebox.showerror("Error", "Invalid response from Image Service")
                return
        else:
            messagebox.showerror("Error", "Image Service did not respond in time")
            return

        # Display the image
        display_image(image_path)

    def display_image(image_path):
        try:
            image = Image.open(image_path)
            image = image.resize((300, 300))  # Resize image for display
            photo = ImageTk.PhotoImage(image)

            label.config(image=photo)
            label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

    # Set up the GUI
    root = tk.Tk()
    root.title("Microservices UI")

    label = tk.Label(root, text="Press the button to display a random image.")
    label.pack(pady=20)

    button = tk.Button(root, text="Generate Image", command=handle_button_click)
    button.pack(pady=10)

    label = tk.Label(root)
    label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    run_ui()
