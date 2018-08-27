#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


class Github:
    SCHEMA = 'https'
    GITHUB_API_HOST = 'api.github.com'
    BASE_URL = SCHEMA + '://' + GITHUB_API_HOST
    ACCEPT_JSON = 'application/vnd.github.v3+json'
    ACCEPT_RAW = 'application/vnd.github.v3.raw'
    CODE_SEARCH_PATH = '/search/code'

    def __init__(self, token):
        self.token = token

    # see https://developer.github.com/v3/search/#search-code
    def search_files(self, repo, filenames):
        paths = []
        query = '?q=repo:' + repo
        for filename in filenames:
            query += '+filename:"' + filename + '"'
        url = Github.BASE_URL + Github.CODE_SEARCH_PATH + query
        header = {
            'Accept': Github.ACCEPT_JSON,
        }
        if self.token:
            header['Authorization'] = 'token ' + self.token
        res = requests.get(url, headers=header)
        for i in res.json()['items']:
            if i['name'] in filenames:
                paths.append(i['path'])
        return paths

    # see https://developer.github.com/v3/repos/contents/#get-contents
    def get_files(self, repo, path):
        url = Github.BASE_URL + Github.__get_content_path(repo, path)
        header = {
            'Accept': Github.ACCEPT_RAW,
        }
        if self.token:
            header['Authorization'] = 'token ' + self.token
        res = requests.get(url, headers=header)
        return res.text

    @staticmethod
    def __get_content_path(repo, path):
        return '/repos/' + repo + '/contents/' + path
