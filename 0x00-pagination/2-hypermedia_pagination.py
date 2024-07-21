#!/usr/bin/env python3
"""
implement named that takes two integer argument with
defaut number and return the list of the specified to index
"""
import csv
import math
from typing import List
import requests  # type: ignore


def download_csv(url: str, filename: str) -> None:
    """
    Download the csv file from the URL and save it locally
    """
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"file downloaded with file name '{filename}'")
    else:
        print(f"failed to download file")


def index_range(page, page_size):
    """
    this function takes two argument
    args:
        -> page
        -> page_size
    return:
        a tuple of size two containing start index and stop idex
    """
    startIndex = (page - 1) * page_size
    endIndex = (page) * page_size
    return startIndex, endIndex


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        this method accept
        args:
            -> page default 1
            -> page_size default 10
        return:
            the list of rows
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        method that takes the same arguments as get_page
        args:
            -> page default 1
            -> page_size default 10
        return
            dictionary with key-value pair
        """
        data_page = self.get_page(page, page_size)
        total_content = len(self.dataset())
        total_pages = math.ceil(total_content / page_size)
        if (page * page_size) < total_content:
            next_page = page + 1
        else:
            None
        if (page > 1):
            prev_page = page - 1
        else:
            None
        return {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
