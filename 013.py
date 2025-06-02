# Convert any image to black & white.

from PIL import Image

img = Image.open("input.jpg")
gray = img.convert("L")
gray.save("output.jpg")
