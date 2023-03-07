import datetime
from datetime import timedelta

left = datetime.datetime(1901, 1, 1)
right = datetime.datetime(2000, 12, 31)

ans = 0
while True :
    if left.weekday() == 6 and left.day == 1 :
        ans += 1
        print(left)
    if left == right :
        break
    left += timedelta(days=1)

print(ans)
