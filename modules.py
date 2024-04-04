def factorial_calc(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_calc(n - 1)