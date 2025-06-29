# Copyright 2025 ( @annuaicoder )
# Check if a URL is online (200 OK) or down.

import requests

url = "https://example.com"
try:
    r = requests.get(url, timeout=5)
    print("Online!" if r.status_code == 200 else f"Issue: {r.status_code}")
except requests.exceptions.RequestException:
    print("Offline or invalid URL")
