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
        libraryの情報を取得します
        返却される値はdict型Objectで、下記の情報が入っています
        (license, author, url)
        """
        pass        
