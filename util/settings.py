#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml

class Settings:

    def __init__(self):
        with open('settings.yml') as f:
            self.settings = yaml.safe_load(f)
