from datetime import date

def get_weekday(date_string):
    day = date.fromisoformat(date_string)
    weekday = day.strftime("%A")

    return weekday

print(get_weekday("1999-12-31"))
