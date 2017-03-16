N = 10
CACHE = [None] * (N+1)


def fib_dyn(n):
    if n == 0 or n == 1:
        return n

    if CACHE[n] != None:
        return CACHE[n]

    CACHE[n] = fib_dyn(n-1) + fib_dyn(n-2)

    return CACHE[n]


def fib_rec(n):
    if n == 0 or n == 1:
        return n

    return fib_rec(n-1) + fib_rec(n-2)


def fib_iter(n):

    if n == 0 or n == 1:
        return n

    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a

def fib_iter_bad(n):
    if n == 0 or n == 1:
        return n

    fibo = [0,1]
    while len(fibo) <= n:
        fibo.append(fibo[-2] + fibo[-1])

    return fibo[-1]

if __name__ == '__main__':
    print(fib_iter(10))