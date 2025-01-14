import random
import time
import os

def prng_service():
    file_path = "prng_service.txt"

    while True:
        # Check if the file exists and contains "run"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                command = file.read().strip()

            if command == "run":
                # Generate a pseudo-random number
                random_number = random.randint(0, 100)  # Example range: 0 to 100

                # Write the random number back to the file
                with open(file_path, "w") as file:
                    file.write(str(random_number))

        # Sleep to prevent excessive CPU usage
        time.sleep(0.1)

if __name__ == "__main__":
    prng_service()
