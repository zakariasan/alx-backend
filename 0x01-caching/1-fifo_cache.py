#!/usr/bin/env python3
"""  Basic dictionary"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching and implements FIFOCache
    caching system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first_key = self.order.pop(0)
                    del self.cache_data[first_key]
                    print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)
            else:
                self.order.remove(key)
                self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
