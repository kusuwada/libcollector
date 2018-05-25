#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Output:
    __metaclass__ = ABCMeta

    def __init__(self, output, data=None, path=None):
        self.output = output
        self.data = data
        self.path = path

    @abstractmethod
    def write(self):
        pass
