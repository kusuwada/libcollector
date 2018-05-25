#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from util import constants


def parse():
    parser = argparse.ArgumentParser(
        description='collect information of the library which used in specified github repositories')
    parser.add_argument('--token', required=False, help='your github access token')  # github_access_token
    parser.add_argument('--version', action='version', version='libcollector ' + constants.VERSION)
    return parser.parse_args()
