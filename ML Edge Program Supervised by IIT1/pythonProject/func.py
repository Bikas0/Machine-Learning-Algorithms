def calculate(n, n1, n2):
    return ((n * n1) % n2) + (n + n1 + n2)


print(calculate(3, 4, 5))
