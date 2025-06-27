# Copyright 2025 ( @annuaicoder )
# Detect duplicate files in a folder (by hash).

import os, hashlib

def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

folder = "your_folder_path"
seen = {}
for f in os.listdir(folder):
    path = os.path.join(folder, f)
    if os.path.isfile(path):
        h = file_hash(path)
        if h in seen:
            print(f"Duplicate: {f} == {seen[h]}")
        else:
            seen[h] = f
