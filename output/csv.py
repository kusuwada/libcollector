#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from output.output import Output


class Csv(Output):

    def __init__(self, output, data=None, path=None):
        super().__init__(output, data, path)

    def write(self):
        with open(self.path, 'w') as f:
            writer = csv.writer(f, delimiter=',', lineterminator='\n')
            writer.writerow(self.data[0].__dict__.keys())
            for item in self.data:
                writer.writerow(item.__dict__.values())
