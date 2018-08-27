#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Index():
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_library_info(self, name):
        """
        return library information.
        return object format is dict, with follow data.
        (license, author, url)
        """
        pass        
