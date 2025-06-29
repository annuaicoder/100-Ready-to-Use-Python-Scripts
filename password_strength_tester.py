# Copyright 2025 ( @annuaicoder )

import re

def password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    # Character variety checks
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add symbols (e.g., !, @, #).")

    # Common weak passwords
    weak_list = ['password', '123456', 'qwerty', 'admin', 'letmein']
    if password.lower() in weak_list:
        score = 0
        feedback = ["This is a very common and unsafe password."]

    return score, feedback

if __name__ == "__main__":
    pwd = input("🔐 Enter a password to test: ")
    score, tips = password_strength(pwd)

    print(f"\n🔎 Strength Score: {score}/6")

    if score >= 5:
        print("✅ Strong password!")
    elif score >= 3:
        print("⚠️ Medium strength — consider improving:")
        for tip in tips:
            print(f"  • {tip}")
    else:
        print("❌ Weak password!")
        for tip in tips:
            print(f"  • {tip}")
