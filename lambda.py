func = lambda x, y, v, b: x * y + v + b
print(func(3, 3, 2, 2))
print(func(4, 3, 2, 2))
print(func(3, 9, 2, 2))
new1 = func
print(new1(3,3,3,3))

