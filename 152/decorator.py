from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    def _outer_wrapper(wrapped_function):
        wraps(wrapped_function)

        def _wrapper(*args, **kwargs):
            text = wrapped_function(*args, **kwargs)

            wrapped_start = start
            wrapped_end = end

            if wrapped_start < 0:
                wrapped_start = 0

            if wrapped_end > len(text):
                wrapped_end = len(text)

            if wrapped_end < 1:
                wrapped_end = 0

            dots = (wrapped_end - wrapped_start) * "."
            # stripped = dots.join([text[:wrapped_start], text[end:]])
            bit_before_stripped = text[0:wrapped_start]
            bit_after_stripped = text[wrapped_end:]
            stripped = bit_before_stripped + dots + bit_after_stripped
            return stripped
        return _wrapper
    return _outer_wrapper


