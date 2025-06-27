# Generate fun ASCII art banners from text.
# Copyright 2025 ( @annuaicoder )

import pyfiglet

text = "Hello"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)
