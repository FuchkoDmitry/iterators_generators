nested_list = [
                ['a', ['b', 8, 0, [1, 4, [9, [5, 5, [6, 2, ['f', 't']]]]]]],
                ['d', 'e', 'f', 'h', [False, [True]]],
                [1, 2, None],
                ]


def flat_generator(iterable_object):
    for nested_object in iterable_object:
        if not isinstance(nested_object, list):
            yield nested_object
        else:
            yield from flat_generator(nested_object)


for item in flat_generator(nested_list):
    print(item)

flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)
