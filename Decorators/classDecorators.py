# class X:
#     def __init__(self):
#         print("An instance or object was initialised")
#
#     def __call__(self, *args, **kwargs):
#         print("Arguments are ", args,kwargs)
#
#
# a = X()
# print("Calling Objects or Arguments")
# a(4,5, z=12, v=20)
#
# print("Calling call function again")
# a(8,9,r =40,t=50)

# ---------------------------------------
#
# def x():
#     print('Doing something using function decorators')
#
#     def y():
#         print('naming ' + x.__name__)
#
#     return y
#
#
# def repeatable():
#     c = x()
#     d = c()
#
#
# repeatable()

# --------------------------------------------

class x:
    def __init__(self):
        print("Doing something using function decorators")

    def __call__(self):
        print('naming ' + x.__name__)


def repeatable():
    c = x()
    c()

repeatable()
