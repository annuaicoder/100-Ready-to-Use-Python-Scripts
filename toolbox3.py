# Copyright 2025 ( @annuaicoder )

import random
import string
import os
import socket

def generate_username():
    adjectives = ['Cool', 'Fast', 'Smart', 'Brave', 'Bright']
    nouns = ['Tiger', 'Eagle', 'Shark', 'Lion', 'Wolf']
    username = random.choice(adjectives) + random.choice(nouns) + str(random.randint(10, 99))
    print("Generated username:", username)

def get_ip_address():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"Your IP address is: {ip}")

def convert_to_uppercase():
    text = input("Enter text to convert to uppercase: ")
    print("Uppercase:", text.upper())

def countdown_timer():
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        import time
        while seconds > 0:
            print(f"Time left: {seconds} seconds", end='\r')
            time.sleep(1)
            seconds -= 1
        print("\nTime's up!")
    except ValueError:
        print("Please enter a valid number.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Console cleared.")

def main():
    while True:
        print("\n=== Swiss Army Knife Tool 3.0 ===")
        print("1. Generate a random username")
        print("2. Get your IP address")
        print("3. Convert text to uppercase")
        print("4. Start a countdown timer")
        print("5. Clear the console")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            generate_username()
        elif choice == '2':
            get_ip_address()
        elif choice == '3':
            convert_to_uppercase()
        elif choice == '4':
            countdown_timer()
        elif choice == '5':
            clear_console()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
