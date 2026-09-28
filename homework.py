import datetime
import re
import random

def get_days_from_today(date):
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        today = datetime.datetime.today()
        difference = today.date() - date.date()
        return difference.days
    except ValueError:
        return "Неправильний формат дати"


def normalize_phone(phone_number):
    phone_number = re.sub(r"[^\d+]", "", phone_number)

    if phone_number.startswith("+38"):
        return phone_number

    if phone_number.startswith("380"):
        return "+" + phone_number

    return "+38" + phone_number



def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min >= max:
        return []

    if quantity < 1 or quantity > (max - min + 1):
        return []

    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)

