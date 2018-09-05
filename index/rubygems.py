#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from index.index import Index
from library_info import LibraryInfo


class RubyGems(Index):
    """
    Ruby gem module index
    https://guides.rubygems.org/rubygems-org-api/
    """

    API_URI = 'https://rubygems.org/api/v1/'

    def __init__(self):
        super().__init__()

    def get_library_info(self, name, version=None):
        info = {}
        # to get license information, version is required
        if not version:
            url = RubyGems.API_URI + 'versions/' + name + '/latest.json'
            res = requests.get(url)
            if res.status_code == 200:
                version = res.json()['version']
            elif res.status_code == 404:
                return info
            else:
                print('When get index of ' + name + ', ' + \
                      res.status_code + ' returned.')
                return info
        # get license information
        url = RubyGems.API_URI + 'versions/' + name + '.json'
        res = requests.get(url)
        if res.status_code == 200:
            for v in res.json():
                if v['number'] == version:
                    info['license'] = ','.join(v['licenses'])
        # get author and uri information
        url = RubyGems.API_URI + 'gems/' + name + '.json'
        res = requests.get(url)
        if res.status_code == 200:
            info['author'] = res.json()['authors']
            info['homepage_url'] = res.json()['homepage_uri']
            info['code_url'] = res.json()['source_code_uri']

        return info
