#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from output.output import Output


class Text(Output):

    def __init__(self, output, data=None, path=None):
        super().__init__(output, data, path)

    def write(self):
        with open(self.path, 'w') as f:
            if len(self.data) > 0:
                for item in self.data:
                    f.write(str(item) + '\n')
