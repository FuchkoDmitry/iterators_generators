nested_list = [
                ['a', ['b', 8, 0, [1, 4, [9, [5, 5, [6, 2, ['f', 't']]]]]]],
                ['d', 'e', 'f', 'h', [False, [True]]],
                [1, 2, None],
                ]


class FlatIterator:

    def __init__(self, iterable_object):
        self.iterable_object = iterable_object

    def nested_list_unpack(self, iterable_object):
        result_list = []
        count = 0
        for nested_objects in iterable_object:
            if isinstance(nested_objects, list):
                count = 1
                for element in nested_objects:
                    result_list.append(element)
            else:
                result_list.append(nested_objects)
        if count:
            return self.nested_list_unpack(result_list)
        return result_list

    def __iter__(self):
        self.start = -1
        self.result_list = self.nested_list_unpack(self.iterable_object)
        self.stop = len(self.result_list)
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.stop:
            raise StopIteration
        return self.result_list[self.start]


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
