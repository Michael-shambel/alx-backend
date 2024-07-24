#!/usr/bin/env python3
"""
applying lifo algorithms on cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    this class will add and get cache item using LIFO algorithm
    """
    def __init__(self):
        super().__init__()
        self.LIFO = []

    def put(self, key, item):
        """
        put the key and item in to dectionary
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.LIFO.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.LIFO.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
