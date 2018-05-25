#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
from datetime import datetime
from util import argparser
from manager import classify_manager
from output import classify_output
from github import Github


def get_manager_from_path(path):
    return path.split('/')[-1].replace('.', '_').lower()

args = argparser.parse()
library_info_list = []
manager_files = []

with open('settings.yml') as f:
    settings = yaml.safe_load(f)

timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

for repo in settings['target_repositories']:

    git = Github(args.token)
    manager_paths = git.search_files(repo, settings['target_manager'])
    for path in manager_paths:
        manager_files.append({'path': path, 'data': git.get_files(repo, path)})

    for file in manager_files:
        manager = classify_manager.new_manager(
            get_manager_from_path(file['path']), file['data'])
        if not manager:
            continue
        lib_list = manager.parse()
        for lib in lib_list:
            lib.timestamp = timestamp
            lib.owner = repo.split('/')[0]
            lib.repo = repo.split('/')[1]
            lib.path = file['path']
            library_info_list.append(lib)

    for info in library_info_list:
        print(info)

    for out in settings['output'].keys():
        output = classify_output.new_output(
            out, library_info_list, settings['output'][out])
        output.write()
