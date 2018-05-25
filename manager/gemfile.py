#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from manager.manager import Manager
from library_info import LibraryInfo


# Not Support Gemfile.lock
class Gemfile(Manager):

    MANAGER_NAME = 'Gemflie'

    def __init__(self, manager, data=None):
        super().__init__(manager, data)

    def parse(self):
        list = []
        lines = self.data.splitlines()
        for line in lines:
            if not line.startswith('gem'):
                continue
            info = LibraryInfo()
            info.manager = Gemfile.MANAGER_NAME
            if ',' not in line:
                info.name = Gemfile.__format_gemfile(line)
            else:
                info.name = str(Gemfile.__format_gemfile(line.split(',')[0]))
                info.version = str(Gemfile.__format_gemfile(line.split(',')[1]))
            list.append(info)
        return list

    @staticmethod
    def __format_gemfile(line):
        return line.strip('gem ').strip("'").strip('"')
