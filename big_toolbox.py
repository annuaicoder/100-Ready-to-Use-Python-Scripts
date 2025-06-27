# Copyright 2025 ( @annuaicoder )

import os
import random
import string
import datetime
import webbrowser
import hashlib
import socket
import platform
import time
import math
import sys

def open_website():
    url = input("Enter website URL (include http:// or https://): ").strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        print("Invalid URL. Make sure it starts with http:// or https://")
        return
    webbrowser.open(url)
    print(f"Opened {url}")

def generate_password():
    length = input("Password length (default 12): ").strip()
    length = int(length) if length.isdigit() else 12
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(chars) for _ in range(length))
    print("Generated password:", pwd)

def get_system_info():
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

def list_directory():
    path = input("Enter directory path (default current directory): ").strip()
    path = path if path else '.'
    if os.path.isdir(path):
        print(f"Listing files in '{path}':")
        for f in os.listdir(path):
            print(f" - {f}")
    else:
        print("Invalid directory.")

def hash_text():
    text = input("Enter text to hash: ")
    print("Choose hash type:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    choice = input("Option (1-3): ").strip()
    import hashlib
    if choice == '1':
        h = hashlib.md5(text.encode()).hexdigest()
    elif choice == '2':
        h = hashlib.sha1(text.encode()).hexdigest()
    elif choice == '3':
        h = hashlib.sha256(text.encode()).hexdigest()
    else:
        print("Invalid choice")
        return
    print(f"Hash: {h}")

def calculate_factorial():
    n = input("Enter a non-negative integer: ").strip()
    if not n.isdigit():
        print("Invalid input.")
        return
    n = int(n)
    print(f"Factorial of {n} is {math.factorial(n)}")

def fibonacci_sequence():
    n = input("How many Fibonacci numbers to generate? ").strip()
    if not n.isdigit():
        print("Invalid input.")
        return
    n = int(n)
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    print(f"Fibonacci sequence ({n} numbers):")
    print(fib[:n])

def roll_dice():
    sides = input("Number of sides on dice (default 6): ").strip()
    sides = int(sides) if sides.isdigit() else 6
    result = random.randint(1, sides)
    print(f"Rolled a {sides}-sided dice: {result}")

def countdown_timer():
    seconds = input("Countdown seconds: ").strip()
    if not seconds.isdigit():
        print("Invalid input.")
        return
    seconds = int(seconds)
    try:
        while seconds > 0:
            print(f"Time left: {seconds} seconds", end='\r')
            time.sleep(1)
            seconds -= 1
        print("\nTime's up!")
    except KeyboardInterrupt:
        print("\nTimer cancelled.")

def word_count():
    text = input("Enter text: ")
    words = text.split()
    print(f"Word count: {len(words)}")

def get_local_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"Local IP Address: {ip}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_program():
    print("Exiting program. Goodbye!")
    sys.exit()

def main():
    while True:
        print("\n=== BIG Swiss Army Knife Tool ===")
        print("1. Open Website")
        print("2. Generate Password")
        print("3. Get System Info")
        print("4. List Directory Contents")
        print("5. Hash Text (MD5, SHA1, SHA256)")
        print("6. Calculate Factorial")
        print("7. Generate Fibonacci Sequence")
        print("8. Roll Dice")
        print("9. Countdown Timer")
        print("10. Word Count")
        print("11. Get Local IP Address")
        print("12. Clear Console")
        print("13. Exit")

        choice = input("Choose an option (1-13): ").strip()

        if choice == '1':
            open_website()
        elif choice == '2':
            generate_password()
        elif choice == '3':
            get_system_info()
        elif choice == '4':
            list_directory()
        elif choice == '5':
            hash_text()
        elif choice == '6':
            calculate_factorial()
        elif choice == '7':
            fibonacci_sequence()
        elif choice == '8':
            roll_dice()
        elif choice == '9':
            countdown_timer()
        elif choice == '10':
            word_count()
        elif choice == '11':
            get_local_ip()
        elif choice == '12':
            clear_console()
        elif choice == '13':
            exit_program()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
