def metafunc():
    print("i am the metaclass function")


class Inherit:

    def func(self):
        print("I am the inherited method")


metaobject = type('meta', (Inherit,), dict(name="sachin", metafunction=metafunc()))

print(type(metaobject))
b = metaobject()
print(type(b))

b.func()