#!/usr/bin/env python3
"""
creating a class FIFOCache that inherits from BaseCaching and
is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    this class inherit BaseCaching and
    have a method which apply put data and get data
    """
    def __init__(self):
        super().__init__()
        self.FIFO = []

    def put(self, key, item):
        """
        this put data in cache_data using FIFO method
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.FIFO.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.FIFO.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        this get data from cache_data using FIFO method
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
