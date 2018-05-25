#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Manager():
    __metaclass__ = ABCMeta

    def __init__(self, manager, data=None):
        self.manager = manager
        self.data = data

    @abstractmethod
    def parse(self):
        pass
