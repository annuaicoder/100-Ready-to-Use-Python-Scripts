# Copyright 2025 ( @annuaicoder )
# Count how often each word appears in a text file.

from collections import Counter

with open("file.txt", "r") as f:
    words = f.read().lower().split()
    counts = Counter(words)

for word, count in counts.most_common(10):
    print(f"{word}: {count}")
