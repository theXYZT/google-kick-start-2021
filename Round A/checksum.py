# Kickstart 2021: Round A, Checksum

import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree


def solve(N, B):
    max_cost = np.sum(B)

    adj = np.zeros((2*N, 2*N), dtype=int)
    for i in range(N):
        for j in range(N):
            k = B[i, j]
            if k:
                adj[i, N+j] = -k

    max_weight = np.sum(minimum_spanning_tree(adj))
    return max_cost + round(max_weight)


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())
    _ = [input() for _ in range(N)]
    B = np.int32([list(map(int, input().split())) for _ in range(N)])
    _ = input()
    _ = input()
    y = solve(N, B)
    print('Case #{}: {}'.format(case, y))
