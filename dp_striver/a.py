def f(n):
    if n < 4:
        return n
    return f(n-1) + f(n-2)
print(f(10))
