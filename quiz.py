def func1(a,b):

    def func2(c,d):
        return c*d
    return func2(a,b)
    return a

print(func1(10,20))