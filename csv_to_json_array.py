# Copyright 2025 ( @annuaicoder )

# Convert a CSV file into a JSON array.

import csv
import json

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
