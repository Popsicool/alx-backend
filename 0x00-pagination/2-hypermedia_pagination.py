#!/usr/bin/env python3
'''
Implement a method named get_page that
takes two integer arguments page with default value 1
and page_size with default value 10.
'''


from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    The function should return a tuple of size two containing
    a start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.
    '''
    start = (page - 1) * page_size
    end = 0
    for i in range(page):
        end += page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''
        initialize the class
        '''
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        data = self.dataset()
        data_len = len(data)
        try:
            idx = index_range(page, page_size)
            return data[idx[0]: idx[1]]
        except BaseException:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        data_len = len(self.dataset())
        data = self.get_page(page, page_size)
        response = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": data_len,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= data_len else None
        }
        return response
