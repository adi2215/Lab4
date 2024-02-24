import datetime as date

datetime_now = date.datetime.now()

datetime_without_microsec = datetime_now.replace(microsecond = 0)

print(datetime_without_microsec)