# Copyright 2025 ( @annuaicoder )

# Get current time in any timezone using pytz.

from datetime import datetime
import pytz

zone = pytz.timezone('Asia/Tokyo')
time = datetime.now(zone)
print("Tokyo time:", time.strftime("%Y-%m-%d %H:%M:%S"))
