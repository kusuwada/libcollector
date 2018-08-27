#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup
from index.index import Index
from library_info import LibraryInfo



class Npmjs(Index):
    """
    Nodejs module index
    https://docs.npmjs.com/
    * this code scrape npmjs website,
      so the website's change will be influence this code.
    """

    API_URI = 'https://www.npmjs.com/package/'

    def __init__(self):
        super().__init__()

    def get_library_info(self, name):
        info = {}
        url = Npmjs.API_URI + name
        res = requests.get(url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            for s in soup.find_all('script'):
                if (s.string and s.string.startswith('window.__context__')):
                    json_data = json.loads(s.string.strip('window.__context__ = '))
                    info_data = json_data['context']['packument']
                    info['license'] = info_data.get('license')
                    if info_data.get('author'):
                        info['author'] = info_data.get('author').get('name')
                    info['homepage_url'] = info_data.get('homepage')
                    info['code_url'] = info_data.get('repository')
        elif res.status_code == 404:
            pass
        else:
            print('When get index of ' + name + ', ' + \
                  res.status_code + ' returned.')
        return info
