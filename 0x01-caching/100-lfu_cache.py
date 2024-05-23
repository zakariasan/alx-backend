#!/usr/bin/env python3
"""  Basic dictionary"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching and ing system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.usage_order.move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lfu_keys = [k for k,
                                v in self.cache_data.items()
                                if self.frequency[k] ==
                                min(self.frequency.values())]
                    lfu_key = min(lfu_keys, key=lambda k: self.usage_order[k])
                    self.cache_data.pop(lfu_key)
                    self.frequency.pop(lfu_key)
                    self.usage_order.pop(lfu_key)
                    print("DISCARD: {}".format(lfu_key))
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.usage_order[key] = None

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
            return self.cache_data[key]
        return None
