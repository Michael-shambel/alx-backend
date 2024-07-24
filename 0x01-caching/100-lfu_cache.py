#!/usr/bin/env python3
"""
applying LFU algorithms on cache
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    This class will add and get cache items using LFU algorithm
    """
    def __init__(self):
        super().__init__()
        