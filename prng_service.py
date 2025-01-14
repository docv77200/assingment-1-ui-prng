# generating random numbers

import os
import random
import time

def prng_service():
    prng_file = "prng_service.txt"
    IMAGE_COUNT = 6  # Total number of images in the dataset

    while True:
        if os.path.exists(prng_file):
            with open(prng_file, "r") as f:
                command = f.read().strip()
            
            if command == "run":
                # Generate a random number
                random_number = random.randint(0, 100)  # Random range can be large
                valid_number = random_number % IMAGE_COUNT  # Map to valid index
                print(f"PRNG Service: Generated random number {random_number}, mapped to {valid_number}")

                # Overwrite the file with the valid random number
                with open(prng_file, "w") as f:
                    f.write(str(valid_number))
        
        time.sleep(1)  # Prevent busy-waiting

if __name__ == "__main__":
    prng_service()









     