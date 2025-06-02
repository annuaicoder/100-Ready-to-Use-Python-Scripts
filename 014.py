# Create a random strong password.

import random
import string

length = 12
chars = string.ascii_letters + string.digits + "!@#$%^&*()"
password = ''.join(random.choice(chars) for _ in range(length))
print("Password:", password)
