nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(iterable_object):
    for nested_object in iterable_object:
        for element in nested_object:
            yield element


for item in flat_generator(nested_list):
    print(item)

flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)
