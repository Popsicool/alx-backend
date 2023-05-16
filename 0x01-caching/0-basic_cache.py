#!/usr/bin/python3
'''
Basic cache
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    class BaseCache inhering from BaseCaching
    '''

    def put(self, key, item):
        '''
        add to cache
        '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''
        get from cache
        '''
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
