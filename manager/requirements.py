#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from library_info import LibraryInfo
from manager.manager import Manager
from index.pypi import Pypi

class Requirements(Manager):

    MANAGER_NAME = 'requirements.txt'
    # see https://www.python.org/dev/peps/pep-0440/#version-specifiers
    VERSION_OPERATORS = ['~=', '==', '!=', '<=', '>=', '<', '>']

    def __init__(self, manager, data=None):
        super().__init__(manager, data)

    def parse(self):
        list = []
        lines = self.data.splitlines()
        for line in lines:
            info = LibraryInfo()
            info.manager = Requirements.MANAGER_NAME
            has_version = False
            for operator in Requirements.VERSION_OPERATORS:
                if operator not in line:
                    continue
                else:
                    info.name = str(line.split(operator)[0])
                    info.version = operator + str(line.split(operator)[1])
                    has_version = True
            if not has_version:
                info.name = line
            if Manager.needIndex:
                pipy = Pypi()
                index_info = pipy.get_library_info(info.name)
                info.license = index_info.get('license')
                info.author = index_info.get('author')
                info.homepage_url = index_info.get('homepage_url')
                info.code_url = index_info.get('code_url')
            list.append(info)
        return list
