# Copyright 2025 ( @annuaicoder )
# Unzip a .zip file to a specified folder.

import zipfile

with zipfile.ZipFile("file.zip", 'r') as zip_ref:
    zip_ref.extractall("extracted_folder")
