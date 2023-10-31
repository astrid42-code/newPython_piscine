import time
import datetime

months = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec',
}

seconds = time.time()
res = f'{seconds:,.4f}'
other_seconds = '{:.2e}'.format(time.time())
myDate = datetime.datetime.today()
month = myDate.month

print("Seconds since January 1, 1970:", res, "or", other_seconds,
      "in scientific notation")
print(months[month], myDate.day, myDate.year)
