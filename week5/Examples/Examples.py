def new_func(x):
    return (lambda y: x + y)
t = new_func(3)
u = new_func(4)
print(t(4))
print(u(3))


#####################################


def x(a): return a + 10
print(x(6))


#####################################


str = input("Enter a String")
upper = 0
lower = 0
for i in range(len(str)):
    if(str[i] >= 'a' and str[i] <= 'z'):
        lower += 1

    elif(str[i] >= 'A' and str[i] <= 'Z'):
        upper += 1
print('Lower case letters =', lower)
print('Upper case letters =', upper)
