from callLimit import callLimit


@callLimit(3)
def f():
    print ("f()")
@callLimit(1)
def g():
     ("g()")
for i in range(3):
    f()
    g()