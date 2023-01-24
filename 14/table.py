import random

names = ['Julian', 'Bob', 'PyBites', 'Dante', 'Martin', 'Rodolfo']
aliases = ['Pythonista', 'Nerd', 'Coder'] * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*args):
    zipped = zip(*args)
    table = [ SEPARATOR.join(map(str, tup)) for tup in zipped ]
    return table

if __name__ == "__main__":
    print(generate_table(names, aliases, points, awake))




