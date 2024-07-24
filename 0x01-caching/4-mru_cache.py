#!/usr/bin/env python3
"""
applying MRU algorithms on cache
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    This class will add and get cache items using MRU algorithm
    """
    def __init__(self):
        super().__init__()
        self.MRU = []

    def put(self, key, item):
        """
        Put the key and item into the dictionary
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.MRU.remove(key)
            self.MRU.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                most_used = self.MRU.pop()
                del self.cache_data[most_used]
                print(f"DISCARD: {most_used}")

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.MRU.remove(key)
        self.MRU.append(key)
        return self.cache_data[key]
