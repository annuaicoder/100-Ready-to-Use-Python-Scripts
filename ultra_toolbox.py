# Copyright 2025 ( @annuaicoder )

import os
import sys
import random
import string
import datetime
import webbrowser
import hashlib
import socket
import platform
import time
import math
import json
import urllib.request
import subprocess
import shutil
from collections import Counter

# --- System Utilities ---

def get_system_info():
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python Version: {platform.python_version()}")

def list_directory():
    path = input("Enter directory path (default current directory): ").strip()
    path = path if path else '.'
    if os.path.isdir(path):
        print(f"Files in '{path}':")
        for f in os.listdir(path):
            full_path = os.path.join(path, f)
            if os.path.isdir(full_path):
                print(f"  [DIR]  {f}")
            else:
                size = os.path.getsize(full_path)
                print(f"  [FILE] {f} - {size} bytes")
    else:
        print("Invalid directory path.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Text Utilities ---

def word_count():
    text = input("Enter text: ")
    words = text.split()
    print(f"Word count: {len(words)}")

def char_frequency():
    text = input("Enter text: ")
    counter = Counter(text)
    print("Character frequencies:")
    for char, count in counter.most_common():
        if char == '\n':
            display_char = "\\n"
        elif char == ' ':
            display_char = "'space'"
        else:
            display_char = char
        print(f"'{display_char}': {count}")

def text_to_hash():
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

def text_to_upper():
    text = input("Enter text: ")
    print("Uppercase:", text.upper())

def text_to_lower():
    text = input("Enter text: ")
    print("Lowercase:", text.lower())

# --- Web Utilities ---

def open_website():
    url = input("Enter website URL (include http:// or https://): ").strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        print("Invalid URL format.")
        return
    webbrowser.open(url)
    print(f"Opened {url}")

def get_public_ip():
    print("Fetching public IP address...")
    try:
        with urllib.request.urlopen('https://api.ipify.org') as response:
            ip = response.read().decode()
            print(f"Public IP Address: {ip}")
    except Exception as e:
        print(f"Error fetching IP: {e}")

# --- Math Utilities ---

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

def prime_check():
    num = input("Enter an integer to check if prime: ").strip()
    if not num.isdigit():
        print("Invalid input.")
        return
    num = int(num)
    if num < 2:
        print(f"{num} is not prime.")
        return
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(f"{num} is not prime.")
            return
    print(f"{num} is prime!")

def gcd_lcm():
    a = input("Enter first integer: ").strip()
    b = input("Enter second integer: ").strip()
    if not (a.isdigit() and b.isdigit()):
        print("Invalid input.")
        return
    a, b = int(a), int(b)
    gcd = math.gcd(a, b)
    lcm = abs(a*b) // gcd if gcd else 0
    print(f"GCD({a}, {b}) = {gcd}")
    print(f"LCM({a}, {b}) = {lcm}")

def basic_calculator():
    print("Basic Calculator (+, -, *, /)")
    expr = input("Enter expression (e.g. 2 + 3): ").strip()
    try:
        result = eval(expr, {"__builtins__": None}, {})
        print(f"Result: {result}")
    except Exception as e:
        print(f"Invalid expression: {e}")

# --- Random Utilities ---

def generate_password():
    length = input("Password length (default 12): ").strip()
    length = int(length) if length.isdigit() else 12
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(chars) for _ in range(length))
    print("Generated password:", pwd)

def roll_dice():
    sides = input("Number of sides on dice (default 6): ").strip()
    sides = int(sides) if sides.isdigit() else 6
    result = random.randint(1, sides)
    print(f"Rolled a {sides}-sided dice: {result}")

def random_username():
    adjectives = ['Cool', 'Fast', 'Smart', 'Brave', 'Bright', 'Mighty', 'Silent', 'Fierce']
    nouns = ['Tiger', 'Eagle', 'Shark', 'Lion', 'Wolf', 'Dragon', 'Phoenix', 'Falcon']
    username = random.choice(adjectives) + random.choice(nouns) + str(random.randint(10, 99))
    print("Generated username:", username)

def random_hex_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    print("Random HEX color code:", color)

# --- File Utilities ---

def create_text_file():
    filename = input("Enter filename to create: ").strip()
    if os.path.exists(filename):
        print("File already exists! Choose another name.")
        return
    content = input("Enter content for the file:\n")
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def read_text_file():
    filename = input("Enter filename to read: ").strip()
    if not os.path.exists(filename):
        print("File does not exist.")
        return
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"--- Content of '{filename}' ---")
        print(content)
        print("--- End of file ---")
    except Exception as e:
        print(f"Error: {e}")

def delete_file():
    filename = input("Enter filename to delete: ").strip()
    if not os.path.exists(filename):
        print("File does not exist.")
        return
    confirm = input(f"Are you sure you want to delete '{filename}'? (y/n): ").strip().lower()
    if confirm == 'y':
        try:
            os.remove(filename)
            print(f"File '{filename}' deleted.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Delete cancelled.")

# --- Time & Date Utilities ---

def current_datetime():
    now = datetime.datetime.now()
    print("Current Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def days_until_date():
    date_str = input("Enter a future date (YYYY-MM-DD): ").strip()
    try:
        future_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.datetime.now()
        delta = future_date - today
        if delta.days >= 0:
            print(f"Days until {date_str}: {delta.days}")
        else:
            print(f"The date {date_str} is in the past.")
    except ValueError:
        print("Invalid date format.")

def countdown_timer():
    seconds = input("Enter countdown time in seconds: ").strip()
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

# --- Network Utilities ---

def get_local_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"Local IP Address: {ip}")

def ping_host():
    host = input("Enter hostname or IP to ping: ").strip()
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '4', host]
    try:
        subprocess.run(command)
    except Exception as e:
        print(f"Error: {e}")

# --- Main Menu ---

def exit_program():
    print("Exiting... Goodbye!")
    sys.exit()

def main():
    actions = {
        '1': ("System Info", get_system_info),
        '2': ("List Directory Contents", list_directory),
        '3': ("Clear Console", clear_console),
        '4': ("Word Count", word_count),
        '5': ("Character Frequency", char_frequency),
        '6': ("Text Hash (MD5, SHA1, SHA256)", text_to_hash),
        '7': ("Text to Uppercase", text_to_upper),
        '8': ("Text to Lowercase", text_to_lower),
        '9': ("Open Website", open_website),
        '10': ("Get Public IP", get_public_ip),
        '11': ("Calculate Factorial", calculate_factorial),
        '12': ("Generate Fibonacci Sequence", fibonacci_sequence),
        '13': ("Prime Number Check", prime_check),
        '14': ("GCD and LCM Calculator", gcd_lcm),
        '15': ("Basic Calculator", basic_calculator),
        '16': ("Generate Password", generate_password),
        '17': ("Roll Dice", roll_dice),
        '18': ("Generate Random Username", random_username),
        '19': ("Generate Random HEX Color", random_hex_color),
        '20': ("Create Text File", create_text_file),
        '21': ("Read Text File", read_text_file),
        '22': ("Delete File", delete_file),
        '23': ("Current Date and Time", current_datetime),
        '24': ("Days Until Date", days_until_date),
        '25': ("Countdown Timer", countdown_timer),
        '26': ("Get Local IP Address", get_local_ip),
        '27': ("Ping Host", ping_host),
        '28': ("Exit Program", exit_program),
    }

    while True:
        print("\n=== MEGA ULTRA SWISS ARMY KNIFE ===")
        for key, (desc, _) in sorted(actions.items()):
            print(f"{key}. {desc}")
        choice = input("Choose an option: ").strip()
        if choice in actions:
            try:
                actions[choice][1]()
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
