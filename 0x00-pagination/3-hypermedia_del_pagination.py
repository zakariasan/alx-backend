#!/usr/bin/env python3
""" Pagination """

import csv
import math
from typing import List, Dict, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                data = [row for row in reader]
            self.__dataset = data[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a specific page of data."""
        assert isinstance(
            page, int) and page > 0, "Page number must be a positive integer."
        assert isinstance(
            page_size, int) and page_size > 0, "Page size must be a positive integer."

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index >= len(data):
            return []

        return data[start_index:end_index]

    def get_hyper_index(self, start_index: int = 0, page_size: int = 10) -> Dict:
        """Retrieve hypermedia pagination info starting from a specific index."""
        data = self.indexed_dataset()
        assert start_index >= 0 and start_index <= max(
            data.keys()), "Start index out of range."

        current_page_data = []
        item_count = 0
        next_index = None

        for index, item in data.items():
            if index >= start_index and item_count < page_size:
                current_page_data.append(item)
                item_count += 1
            elif item_count == page_size:
                next_index = index
                break

        return {
            'index': start_index,
            'next_index': next_index,
            'page_size': len(current_page_data),
            'data': current_page_data,
        }

    def indexed_dataset(self) -> Dict[int, List]:
        """Create a dindexed dataset for deletion-resilient pagination."""
        if self.__dataset is None:
            self.dataset()

        return {i: row for i, row in enumerate(self.__dataset)}
