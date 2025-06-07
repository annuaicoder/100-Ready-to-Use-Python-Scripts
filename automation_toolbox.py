import webbrowser
import random
import string
import os
import datetime

def open_website():
    url = input("Enter website URL (include http:// or https://): ")
    webbrowser.open(url)
    print(f"Opened {url} in your browser.")

def generate_password():
    length = input("Enter password length (default 12): ")
    length = int(length) if length.isdigit() else 12
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated password: {password}")

def get_current_time():
    now = datetime.datetime.now()
    print(f"Current date & time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def list_files():
    path = input("Enter directory path (default current directory): ").strip()
    path = path if path else '.'
    if os.path.exists(path) and os.path.isdir(path):
        print(f"Files in '{path}':")
        for f in os.listdir(path):
            print(f" - {f}")
    else:
        print("Invalid directory path.")

def roll_dice():
    sides = input("Enter number of sides on the dice (default 6): ")
    sides = int(sides) if sides.isdigit() and int(sides) > 1 else 6
    result = random.randint(1, sides)
    print(f"Rolled a {sides}-sided dice: {result}")

def main():
    while True:
        print("\n=== Swiss Army Knife Tool ===")
        print("1. Open a website")
        print("2. Generate a random password")
        print("3. Get current date and time")
        print("4. List files in a directory")
        print("5. Roll a dice")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            open_website()
        elif choice == '2':
            generate_password()
        elif choice == '3':
            get_current_time()
        elif choice == '4':
            list_files()
        elif choice == '5':
            roll_dice()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
