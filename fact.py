def fuct(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fuct(n-1)

print(fuct(6))