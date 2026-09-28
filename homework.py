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

print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2026-10-01"))
print(get_days_from_today("2020/10/09"))


def normalize_phone(phone_number):
    phone_number = re.sub(r"[^\d+]", "", phone_number)

    if phone_number.startswith("+38"):
        return phone_number

    if phone_number.startswith("380"):
        return "+" + phone_number

    return "+38" + phone_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min >= max:
        return []

    if quantity < 1 or quantity > (max - min + 1):
        return []

    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)


lottery_numbers = get_numbers_ticket(1, 49, 6)

print("Ваші лотерейні числа:", lottery_numbers)