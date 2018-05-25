#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class LibraryInfo:
    def __init__(self,
                 timestamp=None,
                 owner=None,
                 repo=None,
                 path=None,
                 manager=None,
                 name=None,
                 version=None):
        self.timestamp = timestamp
        self.owner = owner
        self.repo = repo
        self.path = path
        self.manager = manager
        self.name = name
        self.version = version

    def __repr__(self):
        return 'timestamp: ' + LibraryInfo.__format_for_repr(self.timestamp) + \
               ', owner: ' + LibraryInfo.__format_for_repr(self.owner) + \
               ', repo: ' + LibraryInfo.__format_for_repr(self.repo) + \
               ', path: ' + LibraryInfo.__format_for_repr(self.path) + \
               ', manager: ' + LibraryInfo.__format_for_repr(self.manager) + \
               ', name: ' + LibraryInfo.__format_for_repr(self.name) + \
               ', version: ' + LibraryInfo.__format_for_repr(self.version)

    @staticmethod
    def __format_for_repr(value):
        if not value:
            return 'None'
        return value
