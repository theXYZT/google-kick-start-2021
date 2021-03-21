# Kickstart 2021: Round A, Rabbit House

import numpy as np
from collections import defaultdict


def get_neighbors(i, j, R, C):
    neighbors = []
    if i > 0:
        neighbors.append((i-1, j))

    if i < R-1:
        neighbors.append((i+1, j))

    if j > 0:
        neighbors.append((i, j-1))

    if j < C-1:
        neighbors.append((i, j+1))

    return neighbors


def solve(R, C, grid):
    maxG = np.max(grid)
    minG = maxG - (R + C - 2)
    G = np.where(grid < minG, minG, grid)

    result = np.sum(G - grid)

    buckets = defaultdict(set)
    for i in range(R):
        for j in range(C):
            k = G[i, j]
            buckets[k].add((i, j))

    for k in range(maxG, minG-1, -1):
        if k in buckets:
            nodes = buckets.pop(k)
        else:
            nodes = set()

        for i, j in nodes:
            for x, y in get_neighbors(i, j, R, C):
                g = G[x, y]
                inc = (k - 1) - g
                if inc > 0:
                    G[x, y] += inc
                    result += inc
                    buckets[g].discard((x, y))
                    buckets[g + inc].add((x, y))
    return result


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    R, C = map(int, input().split())
    G = np.array([list(map(int, input().split())) for _ in range(R)])
    y = solve(R, C, np.int64(G))
    print('Case #{}: {}'.format(case, y))
