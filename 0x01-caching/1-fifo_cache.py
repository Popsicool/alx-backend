#!/usr/bin/python3
'''
FIFO caching
'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
    Fifo class
    '''

    def __init__(self):
        ''''
        initialize the class
        '''
        super().__init__()

    def put(self, key, item):
        '''
        put to cache
        '''
        if key and item:
            if key not in self.cache_data.keys():
                if len(self.cache_data) > (BaseCaching.MAX_ITEMS - 1):
                    first_key = list(self.cache_data.keys())[0]
                    print("DISCARD: {}".format(first_key))
                    # del self.cache_data[first_key]
                    self.cache_data.pop(first_key)
            else:
                self.cache_data.pop(key)
            self.cache_data[key] = item

    def get(self, key):
        '''
        get from cache
        '''
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
