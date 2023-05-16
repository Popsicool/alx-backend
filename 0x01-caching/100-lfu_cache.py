#!/usr/bin/python3
'''
LFU caching
'''
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''
    LFU class
    '''

    def __init__(self):
        ''''
        initialize the class
        '''
        self._count = {}
        super().__init__()

    def put(self, key, item):
        '''
        put to cache
        '''
        if key and item:
            if key not in self.cache_data.keys():
                if len(self.cache_data) > (BaseCaching.MAX_ITEMS - 1):
                    min_value = None
                    for k in self.cache_data.keys():
                        if min_value is None or (
                                min_value >= self._count.get(k)):
                            min_value = self._count.get(k)
                    min_keys = [key for key in self.cache_data
                                if self._count[key] == min_value]
                    first_key = min_keys[0]
                    print("DISCARD: {}".format(first_key))
                    # del self.cache_data[first_key]
                    self.cache_data.pop(first_key)
                    self._count[key] = 0
                    self.cache_data[key] = item
                self._count[key] = 0
                self.cache_data[key] = item
            else:
                self.cache_data.pop(key)
                self._count[key] = self._count.get(key) + 1
                self.cache_data[key] = item

    def get(self, key):
        '''
        get from cache
        '''
        if key and key in self.cache_data.keys():
            item = self.cache_data.get(key)
            self.cache_data.pop(key)
            self.cache_data[key] = item
            self._count[key] = self._count.get(key) + 1
            return self.cache_data[key]
        else:
            return None
