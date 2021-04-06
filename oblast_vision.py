x = 20
def sum():
    global x
    x = x + 1
    return 2 * 2

print(sum())
print(x)