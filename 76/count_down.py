from functools import singledispatch


def count_down_string(num_string):
    for i in reversed(range(1,len(num_string)+1)):
        out = num_string[:i]
        print(num_string[:i])


def count_down_list(num_list):
    num_string = ''.join([str(n) for n in num_list])
    count_down_string(num_string)


@singledispatch
def count_down(data_type):
    raise ValueError("Unsupported type!", data_type.__class__)


@count_down.register(int)
def _(num):
    count_down_string(str(num))


@count_down.register(float)
def _(num):
    count_down_string(str(num))


@count_down.register(str)
def _(num):
    count_down_string(num)


@count_down.register(list)
def _(num):
    count_down_list(num)

@count_down.register(set)
def _(num):
    count_down_list(list(num))


@count_down.register(tuple)
def _(num):
    count_down_list(list(num))


@count_down.register(dict)
def _(num):
    count_down_list(list(num.keys()))


@count_down.register(range)
def _(num):
    count_down_list(list(num))


