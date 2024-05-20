#!/usr/bin/env python3
""" Pagination """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ The function should return a tuple """

    s_index = (page - 1) * page_size
    e_index = s_index + page_size
    return s_index, e_index
