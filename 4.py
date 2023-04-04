# Program to find number of day between two dates and find number of hours
from datetime import datetime

date1 = input("Enter the date1:")
date2 = input("Enter the date2:")
date_format = "%d-%m-%Y"

d1 = datetime.strptime(date1,date_format)
d2 = datetime.strptime(date2,date_format)
diff = d2-d1
print(diff.days)
hours = (diff.days) * 24
print(hours)