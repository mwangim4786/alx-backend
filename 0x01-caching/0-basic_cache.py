#!/usr/bin/python3
"""Create BasicCache class that inherits from BaseCaching"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Defines BasicCache """

    def put(self, key, item):
        """ Assign item to dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return value of given key """
        return self.cache_data.get(key)
