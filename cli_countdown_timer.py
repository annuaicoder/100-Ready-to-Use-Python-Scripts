# A simple countdown timer in the terminal.
# Copyright 2025 ( @annuaicoder )

import time

seconds = 10
while seconds:
    print(f"{seconds}...", end="\r")
    time.sleep(1)
    seconds -= 1

print("Time's up!")
