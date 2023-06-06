import datetime
import random
import json
import os


def get_year_from_command_line():
    while True:
        try:
            year_input = input("Enter target year(default: this year): ")
            if year_input.strip() == "":
                return datetime.datetime.now().year
            year = int(year_input)
            if 2000 <= year <= 9999:
                return year
            print("Error: The year should be 2000 between 9999")
        except ValueError:
            print("Error: The year should be Integer")


def get_month_from_command_line():
    while True:
        try:
            month_input = input(
                "Enter target month from 1 to 12 (Enter:all month): ")
            if month_input.strip() == "":
                return 99
            month = int(month_input)
            if 1 <= month <= 12:
                return month
            print("Error: The month should be 1 between 12")
        except ValueError:
            print("Error: The month should be Integer")


def get_day_from_command_line():
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
    while True:
        answer_input = input(
            "Commit number should be rondom? , Enter Y or N: ").upper()
        if answer_input in ["Y", "N"]:
            return answer_input
        print("Error: The answer should be Y or N")


def get_freq_from_command_line(is_freq_random):
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
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        return 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31


def get_data_per_month(target_year, target_month, entered_day,
                       is_freq_random, entered_freq):
    data = []

    if entered_day == 0:  # weekdays
        target_days = [f"{i:02d}" for i in range(1, get_days_in_month(
            target_year, target_month) + 1)
            if datetime.date(target_year, target_month, i).weekday() < 5]
    elif entered_day == 32:  # weekend
        target_days = [f"{i:02d}" for i in range(1, get_days_in_month(
            target_year, target_month) + 1)
            if datetime.datetime(
            target_year, target_month, i).weekday() >= 5]
    elif entered_day == 99:
        target_days = [f"{i:02d}" for i in range(1, get_days_in_month(
            target_year, target_month) + 1)]
    else:
        target_days = [str(entered_day).zfill(2)]

    for day in target_days:
        date_string = f"{target_year}-{target_month:02d}-{day}"
        if is_freq_random == 'Y':
            data.append([date_string, random.randint(1, entered_freq)])
        else:
            data.append([date_string, entered_freq])

    return data


def main():
    target_year = get_year_from_command_line()
    entered_month = get_month_from_command_line()
    entered_day = get_day_from_command_line()
    is_freq_random = is_freq_random_from_command_line()
    entered_freq = get_freq_from_command_line(is_freq_random)
    all_data = []

    if entered_month == 99:  # all month
        for month in range(1, 13):
            data = get_data_per_month(target_year, month, entered_day,
                                      is_freq_random, entered_freq)
            all_data.extend(data)

    else:  # target one month
        all_data = get_data_per_month(target_year, entered_month, entered_day,
                                      is_freq_random, entered_freq)

    json_data = json.dumps(all_data)

    # 実行中のPythonスクリプトの絶対パスを取得
    script_path = os.path.abspath(__file__)

    # スクリプトのディレクトリパスを取得
    script_directory = os.path.dirname(script_path)
    file_path = os.path.join(script_directory, 'data.json')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(json_data)


if __name__ == "__main__":
    main()
