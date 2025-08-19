from datetime import datetime
# from datetime import date
# from datetime import time
from datetime import timedelta

# import datetime

now = datetime.now()
result = datetime.today()

result = now.year
result = now.month
result = now.day
result = now.hour
result = now.minute
result = now.second

result = datetime.ctime(now)
result = datetime.strftime(now, "%Y")
result = datetime.strftime(now, "%B")
result = datetime.strftime(now, "%A")
result = datetime.strftime(now, "%X")
result = datetime.strftime(now, "%d")
result = datetime.strftime(now, "%Y %B %A %X")

t = "19 August 2025 hour 10:20:30"

result = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
# result = result.year
# result = result.day

birthday = datetime(2003, 5, 7, 00, 00, 00)

result = datetime.timestamp(birthday)
result = datetime.fromtimestamp(result)
result = datetime.fromtimestamp(0)

result = now - birthday

# result = result.days
# result = result.seconds
# result = result.microseconds

result = now + timedelta(days=10)
result = now - timedelta(days=10)
result = now + timedelta(days=730)

print(result)
