#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from index.index import Index
from library_info import LibraryInfo


class Pypi(Index):
    """
    Python module index
    https://warehouse.readthedocs.io/api-reference/json/
    """

    API_URI = 'https://pypi.python.org/pypi/'

    def __init__(self):
        super().__init__()

    def get_library_info(self, name):
        info = {}
        url = Pypi.API_URI + name + '/json'
        res = requests.get(url)
        if res.status_code == 200:
            info['license'] = res.json()['info']['license']
            info['author'] = res.json()['info']['author']
            info['homepage_url'] = res.json()['info']['home_page']
            info['code_url'] = res.json()['info']['project_url']
        elif res.status_code == 404:
            pass
        else:
            print('When get index of ' + name + ', ' + \
                  res.status_code + ' returned.')
        return info
