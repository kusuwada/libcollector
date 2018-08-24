#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from library_info import LibraryInfo
from manager.manager import Manager
from index.rubygems import RubyGems


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
            if Manager.needIndex:
                rg = RubyGems()
                index_info = rg.get_library_info(info.name)
                info.license = index_info.get('license')
                info.author = index_info.get('author')
                info.homepage_url = index_info.get('homepage_url')
                info.code_url = index_info.get('code_url')
            list.append(info)
        return list

    @staticmethod
    def __format_gemfile(line):
        return line.strip('gem ').strip("'").strip('"')
