# Kickstart 2021: Round B, Consecutive Primes

import math


def is_prime(n):
    if n < 5:
        return n in (2, 3)

    if (n % 2 == 0) or (n % 3 == 0):
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if (n % i == 0) or (n % (i + 2) == 0):
            return False

    return True


def next_prime(n):
    if n < 2:
        return 2

    prime = n if n % 2 else n - 1
    while True:
        prime += 2
        if is_prime(prime):
            return prime


def solve(Z):
    a = next_prime(int(math.sqrt(Z)) - 300)
    b = next_prime(a)

    while a*b <= Z:
        R = a*b
        a, b = b, next_prime(b)

    return R


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    Z = int(input().strip())
    R = solve(Z)
    print('Case #{}: {}'.format(case, R))
