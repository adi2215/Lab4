import datetime as date

a = date.datetime(2024,2,24,13,45,34)
b = date.datetime(2024,2,24,23,49,55)

print((b-a).total_seconds())