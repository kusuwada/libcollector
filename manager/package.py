#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from manager.manager import Manager
from library_info import LibraryInfo
from index.npmjs import Npmjs


class Package(Manager):

    MANAGER_NAME = 'package.json'
    PACKAGE_KINDS = ['dependencies', 'devDependencies']

    def __init__(self, manager, data=None):
        super().__init__(manager, data)

    def parse(self):
        list = []
        package = json.loads(self.data)
        for kinds in Package.PACKAGE_KINDS:
            if kinds not in package.keys():
                continue
            for lib in package[kinds]:
                info = LibraryInfo()
                info.manager = Package.MANAGER_NAME
                info.name = lib
                info.version = package[kinds][lib]
                if Manager.needIndex():
                    npmjs = Npmjs()
                    index_info = npmjs.get_library_info(info.name)
                    if Manager.needLicense():
                        info.license = index_info.get('license')
                    if Manager.needAuthor():
                        info.author = index_info.get('author')
                    if Manager.needHpUrl():
                        info.homepage_url = index_info.get('homepage_url')
                    if Manager.needCodeUrl():
                        info.code_url = index_info.get('code_url')
                list.append(info)
        return list
