class x:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b


#
# obj1 = x(3, 4)
# print(obj1.sum())


class Addition:
    def __init__(self, *arguments):
        if len(arguments) == 0:
            self.numbers = (0, 0)
        else:
            self.numbers = arguments

    def __add__(self, other):
        sum = tuple(x + y for x, y in zip(self.numbers, other.numbers))
        # (1,5)
        # (2,3)
        # (4,5)
        # (8,1)
        # output = (15, 14)
        return Addition(*sum)

    def __mul__(self, other):
        mul = tuple(x * y for x, y in zip(self.numbers, other.numbers))
        return Addition(*mul)

    def __sub__(self, other):
        sub = tuple(x - y for x, y in zip(self.numbers, other.numbers))
        return Addition(*sub)


obj1 = Addition(2, 3)
obj2 = Addition(4, 5)
obj3 = Addition(6, 7)
obj4 = obj1 + obj2 + obj3
obj5 = obj1 * obj2 * obj3
obj6 = Addition(3, 4)
obj7 = Addition(1, 2)
obj8 = obj6 - obj7
print(obj4.numbers)
print(obj5.numbers)
print(obj8.numbers)


############################################################

class Uni:
    def __init__(self, y):
        self.y = y

    def __neg__(self):
        return self.y

    def __pos__(self):
        return self.y

    def __invert__(self):
        return self.y


if __name__ == "__main__":
    obj1 = Uni(-2)
    print(-obj1)
    print(+obj1)
    print(~obj1)


###########################################################################


class comparison:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.x > other.x

    def __eq__(self, other):
        return self.x == other.x


if __name__ == "__main__":
    obj1 = comparison(2)
    obj2 = comparison(4)
    print(obj1 < obj2)
    print(obj1 > obj2)
    print(obj1 == obj2)


############################################################


class EAO:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({0},{1},{2})".format(self.x, self.y, self.z)

    def __iadd__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return EAO(x, y, z)

    def __isub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return EAO(x, y)


obj1 = EAO(2, 3, 4)
obj1 += EAO(3, 5, 6)
obj2 = EAO(2, 3, 4)
obj2 -= EAO(3, 5, 6)
print(obj1)
print(obj2)


################################################################


class disctionary(dict):
    def __add__(self, other):
        self.update(other)
        return disctionary(self)


dict1 = disctionary({'firstname': "sachin"})
dict2 = disctionary({'lastname': "T"})
print(dict1 + dict2)


###########################################################################

class comp:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.x > other.x

    def __et__(self, other):
        return self.x == other.x


if __name__ == "__main__":
    x = comp(2)
    y = comp(5)
    print(x > y)
    print(x < y)
    print(x == y)


#################################################


class Length_Conversion:
    value = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "in": 0.0254,
             "ft": 0.3048, "yd": 0.9144, "mi": 1609.344}

    def __init__(self, x, value_unit="m"):
        self.x = x
        self.value_unit = value_unit

    def Convert_to_Metres(self):
        return self.x * Length_Conversion.value[self.value_unit]

    def __add__(self, other):
        ans = self.Convert_to_Metres() + other.Convert_to_Metres()
        return Length_Conversion(ans / Length_Conversion.value[self.value_unit], self.value_unit)

    def __str__(self):
        return str(self.Convert_to_Metres)

    def __repr__(self):
        return "Length_Conversion(" + str(self.x) + " , " + self.value_unit + ")"


if __name__ == "__main__":
    obj1 = Length_Conversion(5.5, "yd") + Length_Conversion(1)
    print(repr(obj1))
    print(obj1)
