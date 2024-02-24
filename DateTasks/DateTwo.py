import datetime as date

yesterday = date.datetime.today() - date.timedelta(days = 1)

today = date.datetime.today()

tomorrow = date.datetime.today() + date.timedelta(days = 1)

print("", yesterday,"\n", today,"\n", tomorrow)