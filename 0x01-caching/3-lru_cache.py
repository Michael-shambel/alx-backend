#!/usr/bin/env python3
"""
applying LRU algoritms on cache
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    This class will add and get cache items using LRU algorithm
    """
    def __init__(self):
        super().__init__()
        self.LRU = []
    
    def put(self, key, item):
        """
        Put the key and item into the dictionary
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.LRU.append(key)
            else:
                self.LRU.remove(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_used = self.LRU.pop(0)
                del self.cache_data[least_used]
                print(f"DISCARD: {least_used}")
    
    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
