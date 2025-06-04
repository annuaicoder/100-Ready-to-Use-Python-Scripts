#  Rename all files in a folder with a pattern
# (e.g., img_001.jpg, img_002.jpg, ...).

import os

folder = "your_folder_path"
prefix = "img_"
for i, filename in enumerate(os.listdir(folder), 1):
    ext = os.path.splitext(filename)[1]
    new_name = f"{prefix}{i:03}{ext}"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
