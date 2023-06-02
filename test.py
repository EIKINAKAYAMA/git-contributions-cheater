#!/usr/bin/env python3
import argparse
import os
from datetime import datetime, timedelta
import subprocess
import sys


def arguments(argsval):
    """
    メイン関数です。引数を処理し、リポジトリ名と設定値を取得します。
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-np', '--repo_path', type=str, required=False,
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


def run(commands):
    """
    run command on commandline
    """
    with subprocess.Popen(commands) as process:
        process.wait()


def contribute(date):
    """
    create contribute
    """
    with open(
        os.path.join(os.getcwd(), 'README.md'), 'a', encoding='utf-8'
    ) as file:
        file.write(message(date) + '\n\n')
    run(['git', 'add', '.'])
    run(['git', 'commit', '-m', f'"{message(date)}"',
        '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])


def main(def_args=None):
    """
    main
    """
    if def_args is None:
        def_args = sys.argv[1:]
    args = arguments(def_args)
    repo_path = args.repo_path
    date_string = '2023-11-0'
    commit_num = 10
    if repo_path is not None:
        # get repository name
        start = repo_path.rfind('/') + 1
        end = repo_path.rfind('.')
        repo = repo_path[start:end]

    # Auto generating "git commit"
    os.mkdir(repo)
    os.chdir(repo)
    run(['git', 'init', '-b', 'main'])
    if args.user_name is not None:
        run(['git', 'config', 'user.name', args.user_name])
    if args.user_email is not None:
        run(['git', 'config', 'user.email', args.user_email])
    # yars ago 20:00
    target_date = datetime.strptime(date_string, '%Y-%m-%d')
    date_with_time = target_date.replace(hour=12)

    # for day in (start_date + timedelta(n) for n
    #             in range(365)):

    for m in range(commit_num):
        commit_time = date_with_time + timedelta(minutes=m)
        contribute(commit_time)

    # Auto generating "git push"
    run(['git', 'remote', 'add', 'origin', repo_path])
    run(['git', 'branch', '-M', 'main'])
    run(['git', 'push', '-u', 'origin', 'main'])

    print('\nRepository generation ' +
          '\x1b[6;30;42mcompleted successfully\x1b[0m!')


def message(date):
    """
    メイン関数です。引数を処理し、リポジトリ名と設定値を取得します。
    """
    return date.strftime('Contribution: %Y-%m-%d %H:%M')


if __name__ == "__main__":
    main()
