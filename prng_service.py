import os
import random
import time

def prng_service():
    prng_file = "prng_service.txt"
    IMAGE_COUNT = 6  # Adjust to your image count

    while True:
        if os.path.exists(prng_file):
            with open(prng_file, "r") as f:
                command = f.read().strip()

            if command == "run":
                # Generate a random number
                random_number = random.randint(0, 10) % IMAGE_COUNT
                print(f"PRNG Service: Generated random number {random_number}")

                # Overwrite the file with the valid random number
                with open(prng_file, "w") as f:
                    f.write(str(random_number))
        
        time.sleep(0.1)  # Prevent busy-waiting

if __name__ == "__main__":
    prng_service()
