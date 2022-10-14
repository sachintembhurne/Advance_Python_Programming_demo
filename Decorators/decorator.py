# def outside_function():
#     def inside_function():
#         print("This is inside function")
#
#     print("This is outside function")
#     print('Above we are the statement that are executed before inside function')
#     inside_function()
#     print('Below we are the statement that are printed after inside function')
#
#
# outside_function()


# ---------------------------------------------------------
def addition(a, b):
    def add(x, y):
        return x + y

    sum = 'the sum of two no,s is ' + str(add(a, b))
    return sum


answer = addition(5, 3)
print(answer)


# ----------------------------------------------------------
def x(func):
    print('i am the function x')


def y():
    print('I am the function Y')


x(y())


# -------------------------------------------------------------

def outerFunction(a):
    def innerFunction(b):
        return a + b

    return innerFunction


z = outerFunction(2)
v = outerFunction(3)

ans1 = z(4)
ans2 = v(5)
print(ans1)
print(ans2)

# -----------------------------------------
def poly(a,b,c):
    def pol(x):
        return a*x**2 + b*x + c
    return pol

result1 = poly(1,2,3)
result2 = result1(4)
print(result2)

