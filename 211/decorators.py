from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    @wraps(func)
    def _wrapped(*arg, **kwargs):

        tries = 0

        while tries < MAX_RETRIES:
            try:
                result = func(*arg, **kwargs)
                return result
            except Exception as exc:
                print(exc)
                tries += 1

        raise MaxRetriesException
    return _wrapped


