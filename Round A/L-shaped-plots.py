# Kickstart 2021: Round A, L-Shaped Plots

import numpy as np


def get_segments(grid):
    def f(G):
        x = G.copy()
        for i in range(1, len(x)):
            x[i] = np.where(G[i], x[i-1] + 1, 0)
        return x

    return [np.rot90(f(np.rot90(grid, k)), -k) for k in range(4)]


def solve(R, C, grid):
    def count(a, b):
        g = (np.minimum(a // 2, b) + np.minimum(b // 2, a) - 2)
        return np.sum(g * ((a > 1) & (b > 1)))

    T, R, B, L = get_segments(grid)
    return count(T, L) + count(T, R) + count(B, L) + count(B, R)


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    R, C = map(int, input().split())
    grid = np.array([list(map(int, input().split())) for _ in range(R)])
    y = solve(R, C, grid)
    print('Case #{}: {}'.format(case, y))
