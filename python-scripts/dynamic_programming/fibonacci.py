from typing import Set


def fibo(n: int, cache: dict = {}) -> int:
    cache = cache
    if n == 0 or n == 1:
        return n
    if cache.get(n) != None:
        return cache[n]
    cache[n] = fibo(n - 1, cache) + fibo(n - 2, cache)

    return cache.get(n)


print(fibo(10))
