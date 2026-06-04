class Integer:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return Integer_Iterator(self)


class Integer_Iterator:

    def __init__(self, integer):
        self.integer = integer
        self.i = 0
        self.separate_digits()

    def separate_digits(self):
        value = self.integer.data
        self.mylist = [int(e) for e in str(value)]

    def __next__(self):
        if self.i == len(self.mylist):
            raise StopIteration

        current_value = self.mylist[self.i]
        self.i += 1
        return current_value


# usage
x = Integer(1234)

for i in x:
    print(i)


#---- OUTPUT -----

1
2
3
4

