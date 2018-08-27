#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from util.settings import Settings
from abc import ABCMeta, abstractmethod

class Manager():
    __metaclass__ = ABCMeta

    def __init__(self, manager, data=None):
        self.manager = manager
        self.data = data

    @abstractmethod
    def parse(self):
        pass

    def needIndex():
        conf = Settings().settings
        if conf['info_license'] == True or \
           conf['info_homepage_url'] == True or \
           conf['info_code_url'] == True or \
           conf['info_author'] == True:
            return True
        return False
