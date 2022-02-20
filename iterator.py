nested_list = [
                ['a', 'b', 'c'],
                ['d', ['e'], 'f', 'h', False],
                [1, 2, None],
                ['a', 'b', 'c'],
                [1, 2, None],
                ['d', 'e', 'f', 'h', False],
                ]


class FlatIterator:

    def __init__(self, iterable_object):
        self.iterable_object = iterable_object
        self.cursor = 0
        self.nested_cursor = -1

    def __iter__(self):
        return self

    def __next__(self):

        while self.nested_cursor < len(self.iterable_object[self.cursor]) - 1:
            self.nested_cursor += 1
            return self.iterable_object[self.cursor][self.nested_cursor]
        else:
            self.nested_cursor = 0
            self.cursor += 1
            if self.cursor == len(self.iterable_object):
                raise StopIteration

            return self.iterable_object[self.cursor][self.nested_cursor]


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
