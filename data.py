import datetime
import random
import json


def get_year_from_command_line():
    """
    Set target year
    """
    while True:
        try:
            year_input = input("Enter target year(default: this year): ")
            if year_input.strip() == "":
                return datetime.datetime.now().year
            year = int(year_input)
            if 2000 <= year <= 9999:
                return year
            print("Error: The target year should be 2000 between 9999")
        except ValueError:
            print("Error: The taget year should be Integer")


def get_month_from_command_line():
    """
    Set target month
    """
    while True:
        try:
            month_input = input(
                "Enter target month from 1 to 12 (Enter:every month): ")
            if month_input.strip() == "":
                return 99
            month = int(month_input)
            if 1 <= month <= 12:
                return month
            print("Error: The target year should be 1 between 12")
        except ValueError:
            print("Error: The taget year should be Integer")


def get_day_from_command_line():
    """
    Set target day
    """
    while True:
        try:
            day_input = input(
                "Enter day(Enter: alldays, 0: weekdays, 32: weekend): ")
            if day_input.strip() == "":
                return 99
            day = int(day_input)
            if 0 <= day <= 32:
                return day
            print("Error: The day should be 0 between 32")
        except ValueError:
            print("Error: The day should be Integer")


def is_freq_random_from_command_line():
    """
    Get freq random or not.
    """
    while True:
        answer_input = input(
            "Commit number should be rondom? , Enter Y or N: ").upper()
        if answer_input in ["Y", "N"]:
            return answer_input
        print("Error: The answer should be Y or N")


def get_freq_from_command_line(is_freq_random):
    """
    Set frequency
    """
    while True:
        try:
            if is_freq_random == 'Y':
                freq_input = input(
                    "Enter random max commit number(Enter: 10): ")
            else:
                freq_input = input(
                    "Enter fixed commit number(Enter: 10): ")

            if freq_input.strip() == "":
                return 10
            return int(freq_input)
        except ValueError:
            print("Error: The commit number should be Integer")


def get_days_in_month(year, month):
    """
    Set target day
    """
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        return 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31


def main():
    """
    main
    """
    # Set target year
    year = get_year_from_command_line()
    month = get_month_from_command_line()
    day = get_day_from_command_line()
    is_freq_random = is_freq_random_from_command_line()
    freq = get_freq_from_command_line(is_freq_random)

    data = []

    if month == 99:
        days = [str(i) for i in range(
            1, 367 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
            else 366)]
    elif day == 0:
        days = [str(i) for i in range(1, 32) if datetime.datetime(
            year, month, i).weekday() < 5]
    elif day == 32:
        days = [str(i) for i in range(1, 32) if datetime.datetime(
            year, month, i).weekday() >= 5]
    else:
        days = [str(i) for i in range(1, get_days_in_month(year, month) + 1)]

    for day in days:
        date_string = f"{year}-{month:02d}-{day:02d}"
        if is_freq_random == 'Y':
            data.append([date_string, random.randint(1, freq)])
        else:
            data.append([date_string, freq])

    # dataをJSON形式に変換
    json_data = json.dumps(data)

    # data.jsonファイルにJSONデータを書き込む
    with open('data.json', 'w', encoding='utf-8') as file:
        file.write(json_data)


if __name__ == "__main__":
    main()
