# def outer_function(a):
#     def inner_function(b):
#         return a + b
#     return inner_function
#
#
# def repeatable(b):
#     x = outer_function("Hello ")
#     d =x(b)
#     print(d)
#
#
# repeatable("Sachin")
# repeatable("T")


# --------------------------------
# def join(function):
#     function.data = 2
#     return function
#
#
# def add(x, y):
#     return x + y + add.data
#
# join(add)
# c = add(5, 4)
# print(c)
# join(add)
# print(add.data)

# # -------------------------
#
# def x(a):
#     validate_a = 'hello '
#     if a is not validate_a:
#         a = validate_a
#
#     def y(b):
#         validate_b = 'sachin'
#         if b is not validate_b:
#             b = validate_b
#
#         return a + b
#
#     return y
#
#
# def repeatable(a, b):
#     c = x(a)
#     d = c(b)
#     print(d)
#
#
# repeatable('dfsdrg ', 'tttttt')

# -----------------------------------

def argument(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not a positive value")

def factorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)

z = factorial(3)
print(z)