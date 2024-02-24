import datetime as date
current_date = date.datetime.today()
past_date = date.datetime.today() - date.timedelta(days = 5)

print(past_date)