def rec(i, n):
    if i > n:
        return
    else:
        i = i * 2
        print(i)
        rec(i, n)

rec(1, 100)
def sum(x):
    return x * x
print(sum(sum(sum(2))))
print(2**8)