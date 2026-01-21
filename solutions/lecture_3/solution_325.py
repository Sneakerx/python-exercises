"""Prints the current time."""

import datetime

time = datetime.datetime.now()
print(time.strftime("%d.%m.%Y %H:%M:%S"))
