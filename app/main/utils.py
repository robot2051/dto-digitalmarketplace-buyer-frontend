# Some handy methods that can be reused in other stuff
import math
from threading import Thread
from flask.ctx import copy_current_request_context


def get_page_list(page_size, result_size, current_page):
    """
    returns the list of pages. For example if the current page is 8:- [1, ..., 7, 8, 9, ..., 16]
    """
    pages = []

    last_page = int(math.ceil(float(result_size) / float(page_size)))

    pages.append(1)

    if current_page - 2 > 1:
        pages.append('...')

    if current_page - 1 > 1:
        pages.append(current_page - 1)

    if current_page != 1 and current_page <= last_page:
        pages.append(current_page)

    if result_size > current_page * page_size:
        pages.append(current_page + 1)

    if result_size > (current_page + 2) * page_size:
        pages.append('...')

    if result_size > (current_page + 1) * page_size:
        pages.append(last_page)  # last page

    return pages


def run_async(func):
    """
    function decorator, intended to make "func" run in a separate
    thread (asynchronously).
    Returns the created Thread object

    Example-
    @run_async
    def task1():
        do_something
    """
    def wrapper(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
    return wrapper
