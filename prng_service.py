import os
import random
import time

def prng_service():
    prng_file = "prng_service.txt"
    IMAGE_COUNT = 6

    while True:
        if os.path.exists(prng_file):
            with open(prng_file, "r") as f:
                command = f.read().strip()
                print(f"PRNG Service: Read command '{command}' from {prng_file}")

            if command == "run":
                print("PRNG Service: Detected 'run' command")

                # Seed the random number generator dynamically
                random.seed(time.time())  # Seed with current time
                random_number = random.randint(0, 100) % IMAGE_COUNT
                print(f"PRNG Service: Generated random number {random_number}")

                # Overwrite the file with the random number
                with open(prng_file, "w") as f:
                    f.write(str(random_number))
                    print(f"PRNG Service: Wrote random number {random_number} to {prng_file}")
            elif command.isdigit():
                # Skip processing if the file already contains a random number
                print(f"PRNG Service: File already contains random number '{command}'. Skipping...")
        
        time.sleep(0.1)  # Prevent busy-waiting

if __name__ == "__main__":
    prng_service()
