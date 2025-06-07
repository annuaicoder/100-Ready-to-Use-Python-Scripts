import os
import random
import string
import hashlib
import datetime

def text_to_hash():
    text = input("Enter text to hash (MD5): ")
    hash_object = hashlib.md5(text.encode())
    print(f"MD5 hash: {hash_object.hexdigest()}")

def count_words():
    text = input("Enter text to count words: ")
    words = text.split()
    print(f"Word count: {len(words)}")

def random_color_code():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    print(f"Random HEX color code: {color}")

def create_file():
    filename = input("Enter filename to create: ")
    content = input("Enter content for the file: ")
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

def days_until_date():
    date_str = input("Enter a future date (YYYY-MM-DD): ")
    try:
        future_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.datetime.now()
        delta = future_date - today
        if delta.days >= 0:
            print(f"Days until {date_str}: {delta.days} day(s)")
        else:
            print(f"The date {date_str} is in the past.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    while True:
        print("\n=== Swiss Army Knife 2.0 ===")
        print("1. Generate MD5 hash from text")
        print("2. Count words in text")
        print("3. Generate random HEX color code")
        print("4. Create a text file")
        print("5. Calculate days until a future date")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            text_to_hash()
        elif choice == '2':
            count_words()
        elif choice == '3':
            random_color_code()
        elif choice == '4':
            create_file()
        elif choice == '5':
            days_until_date()
        elif choice == '6':
            print("Bye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
