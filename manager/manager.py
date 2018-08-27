#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from util.settings import Settings
from abc import ABCMeta, abstractmethod

class Manager():
    __metaclass__ = ABCMeta
    conf = Settings().settings

    def __init__(self, manager, data=None):
        self.manager = manager
        self.data = data

    @abstractmethod
    def parse(self):
        pass

    def needIndex():
        if Manager.conf['info_license'] == True or \
           Manager.conf['info_author'] == True or \
           Manager.conf['info_homepage_url'] == True or \
           Manager.conf['info_code_url'] == True:
            return True
        return False

    def needLicense():
        if Manager.conf['info_license'] == True:
            return True
        return False

    def needAuthor():
        if Manager.conf['info_author'] == True:
            return True
        return False

    def needHpUrl():
        if Manager.conf['info_homepage_url'] == True:
            return True
        return False

    def needCodeUrl():
        if Manager.conf['info_code_url'] == True:
            return True
        return False
