from callLimit import callLimit

@callLimit(3)
def f():
    print ("f()")

@callLimit(1)
def g():
    print ("g()")
    for i in range(3):
        f()
        g()


# Expected output:

# f()
# g()
# f()
# Error: <function g at 0x7fabdc243ee0> call too many times
# f()
# Error: <function g at 0x7fabdc243ee0> call too many times

# examples of @callLimit with decorators :
# https://zestedesavoir.com/forums/sujet/1346/exercice-python-les-decorateurs/
