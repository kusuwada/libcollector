#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from manager.requirements import Requirements
from manager.gemfile import Gemfile
from manager.package import Package


def new_manager(manager, data):
    if manager == 'requirements_txt':
        return Requirements(manager, data)
    elif manager == 'gemfile':
        return Gemfile(manager, data)
    elif manager == 'package_json':
        return Package(manager, data)
    else:
        print(manager + 'is not supported.')
        return None
