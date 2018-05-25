#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from output.csv import Csv
from output.text import Text


def new_output(output, data, path):
    if output == 'csv':
        return Csv(output, data, path)
    if output == 'text':
        return Text(output, data, path)
    else:
        print(output + 'is not supported.')
        return None
