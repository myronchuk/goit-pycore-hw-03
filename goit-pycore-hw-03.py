import datetime

date_string = input("Today's date (YYYY-MM-DD): ")
date_datetime= datetime.strptime(date_string, "%Y-%m-%d")
print(f{date_datetime})


= datetime.datetime.now()
def get_days_from_today(date)