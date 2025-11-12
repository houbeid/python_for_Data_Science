import time
from datetime import datetime

seconds = time.time()
print(f"Seconds since January 1, 1970: {seconds:.4e}")
current_date = datetime.now().strftime("%b %d %Y")
print(current_date)