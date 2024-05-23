#!/usr/bin/env python3
"""  Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Create a class BasicCache that inherits from BaseCaching and is a"""

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data the item value"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Must return the value in self.cache_data linked to key."""
        return self.cache_data.get(key, None)
