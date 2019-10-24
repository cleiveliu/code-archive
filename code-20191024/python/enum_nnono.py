from enum import IntEnum


class Status(IntEnum):
    OK = 200
    NOT_FOUND = 404
    ERORR = 500


def ok(response):
    pass


def erorr(response):
    pass


def not_found(response):
    pass


def just_do_it(response):
    if response.status_code == Status.OK:
        ok(response)
    elif response.status_code == Status.ERORR:
        erorr(response)
    elif response.status_code == Status.NOT_FOUND:
        not_found(response)
