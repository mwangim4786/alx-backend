#!/usr/bin/python3
""" Creates a class FIFOCache that inherits from BaseCaching and
    is a caching system:
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Defines class FIFOCache """

    def __init__(self):
        """ Initializes FIFOCache """
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """ Assign item to dictionary """
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
