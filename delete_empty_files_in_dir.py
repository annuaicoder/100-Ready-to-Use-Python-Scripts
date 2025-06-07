# Deletes all empty files in a directory.

import os

folder = "your_folder_path"
for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    if os.path.isfile(path) and os.path.getsize(path) == 0:
        os.remove(path)
