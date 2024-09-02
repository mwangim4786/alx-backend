#!/usr/bin/env python3
""" Implement a method named get_page that takes two integer arguments
    page with default value 1 and page_size with default value 10.
"""

import csv
import math
from typing import Tuple
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        """ Output page of dataset. """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
    
        tuple = index_range(page, page_size)
        start = tuple[0]
        end = tuple[1]
        
        try:
            return self.dataset()[start:end]
        except IndexError:
            return []



def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return in a list for pagination parameters. """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)

