from contextlib import contextmanager

class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    @contextmanager
    def __account__(self, *args, **kwargs):
        old_balance = self.balance
        maybe_new_balance = old_balance + args
        if maybe_new_balance >= 0:
            yield maybe_new_balance

        yield old_balance

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager

