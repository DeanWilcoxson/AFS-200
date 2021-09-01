def new_func(x):
    return (lambda y: x * y)

t = new_func(3)
print(t(4))
