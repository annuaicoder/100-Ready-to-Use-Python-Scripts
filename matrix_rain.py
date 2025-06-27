# Copyright 2025 ( @annuaicoder )

import random
import shutil
import time
import os
import sys

def matrix_rain():
    columns, _ = shutil.get_terminal_size()
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&*()"
    drops = [0] * columns

    while True:
        print("\033[1;40m", end="")  # Set background to black
        for i in range(columns):
            char = random.choice(chars)
            if drops[i] == 0:
                if random.random() > 0.975:
                    drops[i] = 1
            if drops[i] != 0:
                print(f"\033[92m{char}", end="")  # Green text
                drops[i] += 1
                if drops[i] > random.randint(5, 15):
                    drops[i] = 0
            else:
                print(" ", end="")
        print()
        time.sleep(0.05)

        try:
            sys.stdout.flush()
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    try:
        os.system("cls" if os.name == "nt" else "clear")
        matrix_rain()
    except KeyboardInterrupt:
        print("\n🌧️ Matrix rain stopped.")
