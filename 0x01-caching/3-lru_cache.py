#!/usr/bin/env python3
"""  Basic dictionary"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching and implements"""

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(discarded[0]))

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
