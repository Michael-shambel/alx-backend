#!/usr/bin/env python3
"""
class BasicCache that inherits from BaseVaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    creating a method put and get that do some specific tasks
    """
    def put(self, key, item):
        """
        this method put key and item in the dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        this method get item by the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
