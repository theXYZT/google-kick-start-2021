# Kickstart 2021: Round A, L-Shaped Plots

import numpy as np


def get_segments(R, C, grid):
    top = np.zeros((R, C), dtype=int)
    top[0] = grid[0]
    for i in range(1, R):
        top[i] = np.where(grid[i], top[i - 1] + 1, 0)

    left = np.zeros((R, C), dtype=int)
    left[:, 0] = grid[:, 0]
    for j in range(1, C):
        left[:, j] = np.where(grid[:, j], left[:, j - 1] + 1, 0)

    bottom = np.zeros((R, C), dtype=int)
    bottom[-1] = grid[-1]
    for i in range(R - 2, -1, -1):
        bottom[i] = np.where(grid[i], bottom[i + 1] + 1, 0)

    right = np.zeros((R, C), dtype=int)
    right[:, -1] = grid[:, -1]
    for j in range(C - 2, -1, -1):
        right[:, j] = np.where(grid[:, j], right[:, j + 1] + 1, 0)

    return top, left, bottom, right


def solve(R, C, grid):
    def count(a, b):
        f = (a > 1) & (b > 1)
        g = (np.minimum(a // 2, b) + np.minimum(b // 2, a) - 2)
        return np.sum(f * g)

    top, left, bottom, right = get_segments(R, C, grid)

    A, B = count(top, left), count(top, right)
    C, D = count(bottom, left), count(bottom, right)
    return A + B + C + D


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    R, C = map(int, input().split())
    grid = np.array([list(map(int, input().split())) for _ in range(R)])
    y = solve(R, C, grid.astype(bool))
    print('Case #{}: {}'.format(case, y))
