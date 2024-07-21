#!/usr/bin/env python3
"""
function that takes two argument and return
a tuble of size two containing a start index and end index
"""


def index_range(page, page_size):
    """
    this function takes two argument
    args:
        -> page
        -> page_size
    return:
      a tuple of size two containing start index and stop idex
    """
    startIndex = (page - 1) * page_size
    endIndex = (page) * page_size
    return startIndex, endIndex
