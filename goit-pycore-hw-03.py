from datetime import datetime
date = input("Введіть дату у форматі 'YYYY-MM-DD':, ")
def get_days_from_today(date: str) -> int:
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'.")
    print (delta.days)