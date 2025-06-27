# Calculate how many days remain until a future date.
# Copyright 2025 ( @annuaicoder )

from datetime import datetime

target = datetime(2025, 12, 31)
today = datetime.today()
diff = target - today
print(f"{diff.days} days remaining.")
