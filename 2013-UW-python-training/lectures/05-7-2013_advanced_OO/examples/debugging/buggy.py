#!/usr/bin/env python

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from decorators.decorators import logger

@logger
def add(x,y):
    result = x + y + 1
    return result
