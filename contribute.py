#!/usr/bin/env python3

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta


def arguments(argsval):
    parser = argparse.ArgumentParser()
    parser.add_argument('-np', '--repo_path', type=str, required=True,
                        help="""A link on an empty non-initialized remote git
                        repository. If specified, the script pushes the changes
                        to the repository. The link is accepted in SSH or HTTPS
                        format. For example: git@github.com:user/repo.git or
                        https://github.com/user/repo.git""")
    parser.add_argument('-un', '--user_name', type=str, required=False,
                        help="""Overrides user.name git config.
                        If not specified, the global config is used.""")
    parser.add_argument('-ue', '--user_email', type=str, required=False,
                        help="""Overrides user.email git config.
                        If not specified, the global config is used.""")
    return parser.parse_args(argsval)


def validate_data(json_data):
    for data in json_data:
        if len(data) != 2:
            return 'Wrong array format'
        date, freq = data
        if not isinstance(date, str) or not isinstance(freq, int):
            return 'Worng data type, it should be [String, Integer]'
        if freq < 1:
            return 'Wrong frequency, it should be 0 < value'
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return 'Worng date format'
    return True


def run(commands):
    with subprocess.Popen(commands) as process:
        process.wait()


def message(date):
    return date.strftime('Contribution: %Y-%m-%d %H:%M')


def contribute(date):
    with open(
        os.path.join(os.getcwd(), 'README.md'), 'a', encoding='utf-8'
    ) as file:
        file.write(message(date) + '\n\n')
    run(['git', 'add', '.'])
    run(['git', 'commit', '-m', f'"{message(date)}"',
        '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])


def main(def_args=None):
    if def_args is None:
        def_args = sys.argv[1:]
    args = arguments(def_args)
    repo_path = args.repo_path
    if repo_path is not None:
        # get repository name
        start = repo_path.rfind('/') + 1
        end = repo_path.rfind('.')
        repo = repo_path[start:end]

    json_file = 'data/data.json'
    with open(json_file, encoding='utf-8') as file:
        json_data = json.load(file)

    # Check data.json format
    validate_result = validate_data(json_data)
    if validate_data(json_data) is not True:
        print(validate_result, file=sys.stderr)
        sys.exit(1)

    # Auto generating "git commit"
    os.mkdir(repo)
    os.chdir(repo)
    run(['git', 'init', '-b', 'main'])
    if args.user_name is not None:
        run(['git', 'config', 'user.name', args.user_name])
    if args.user_email is not None:
        run(['git', 'config', 'user.email', args.user_email])

    for data in json_data:
        date, freq = data
        date_time = datetime.strptime(
            date, '%Y-%m-%d').replace(hour=0)
        for minutes in range(freq):
            commit_time = date_time + timedelta(minutes=minutes)
            contribute(commit_time)

    print('\nAuto commited repository is generated ' +
          '\x1b[6;30;42mcompleted successfully\x1b[0m!')

    # Auto generating "git push"
    run(['git', 'remote', 'add', 'origin', repo_path])
    run(['git', 'branch', '-M', 'main'])
    run(['git', 'push', '-u', 'origin', 'main'])


if __name__ == "__main__":
    main()
