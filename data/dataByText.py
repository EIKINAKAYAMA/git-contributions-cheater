import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta
from typing import Dict, Iterable

from font_data import create_fonts


def arguments(argsval):
    parser = argparse.ArgumentParser()
    parser.add_argument('-sd', '--start_date', type=str, required=True,
                        help="""Set start date of your commit text""")
    parser.add_argument('-ct', '--commit_text', type=str, required=True,
                        help="""Set the text of what you describe
                        on your contributions graph""")
    parser.add_argument('-ue', '--commit_number', type=str, required=False,
                        help="""You can costmize your text's line wight
                        by setting commit_number. Default setting is 1""")
    return parser.parse_args(argsval)


def read_fonts() -> Dict[str, bytes]:
    return read_fonts.create()


def convert_bitmap(fonts: Dict[str, bytes], message: str) -> bytes:
    bitmap = bytearray()
    for ch in message:
        if ch in fonts:
            bitmap += fonts[ch]
    return bytes(bitmap)


def show_bitmap(bitmap: bytes) -> None:
    for i in range(7):
        mask = 1 << i
        for b in bitmap:
            ch = "#" if b & mask else " "
            print(ch, end="")
        print()


def target_days(bitmap: bytes) -> Iterable[int]:
    days = 0
    for b in bitmap:
        for i in range(7):
            if b & (1 << i):
                yield days
            days += 1


def main(def_args=None):
    if def_args is None:
        def_args = sys.argv[1:]
    args = arguments(def_args)
    start_day = args.start_date
    commit_text = args.commit_text
    commit_number = args.commit_number
    if commit_number is None:
        commit_number = 1

    # Check start_day type
    if not re.match(r'\d{4}-\d{2}-\d{2}', start_day):
        sys.exit(f"{start_day} is not type of 'YYYY-MM-DD'")
    try:
        date_obj = datetime.strptime(start_day, '%Y-%m-%d')
    except ValueError:
        sys.exit(f"{start_day} is invalid day")
    if date_obj.year < 2000:
        sys.exit(f"{start_day}'s year should be more than 2000")

    fonts = create_fonts()
    bitmap = convert_bitmap(fonts, commit_text)

    data = []

    for days in target_days(bitmap):
        calculated_date = date_obj + timedelta(days=days)
        data.append([calculated_date.strftime('%Y-%m-%d'), commit_number])

    json_data = json.dumps(data)

    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)
    file_path = os.path.join(script_directory, 'data.json')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(json_data)


if __name__ == "__main__":
    main()
