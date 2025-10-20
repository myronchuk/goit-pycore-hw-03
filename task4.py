from datetime import datetime, timedelta
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming = []
    for user in users:
        bday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        this_year_bday = bday.replace(year=today.year)
        if this_year_bday < today:
            this_year_bday = this_year_bday.replace(year=today.year + 1)
        delta_days = (this_year_bday - today).days
        if 0 <= delta_days <= 6:
            congr_date = this_year_bday
            if congr_date.weekday() == 5:  
                congr_date += timedelta(days=2)
            elif congr_date.weekday() == 6:  
                congr_date += timedelta(days=1)
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congr_date.strftime("%Y.%m.%d")
            })
    return upcoming
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
