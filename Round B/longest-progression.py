# Kickstart 2021: Round B, Longest Progression

import itertools
from collections import namedtuple

Chunk = namedtuple("Chunk", ["k", "d"])


def solve(N, A):
    if N <= 3:
        return N

    D = [A[i] - A[i-1] for i in range(1, N)]
    chunks = [Chunk(len(list(g)), d) for d, g in itertools.groupby(D)]

    best = 1
    for i, z in enumerate(chunks):
        best = max(best, z.k)
        if i > 0 or i < len(chunks) - 1:
            best = max(best, z.k + 1)

        if i > 1:
            x, y = chunks[i-2], chunks[i-1]

            if y.k == 1 and x.d + y.d == 2 * z.d:
                best = max(best, z.k + 2)

                if i > 2 and x.k == 1 and z.d == chunks[i-3].d:
                    best = max(best, z.k + 2 + chunks[i-3].k)

        if i < len(chunks) - 2:
            a, b = chunks[i+1], chunks[i+2]

            if a.k == 1 and a.d + b.d == 2 * z.d:
                best = max(best, z.k + 2)

    return best + 1


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input().strip())
    A = list(map(int, input().split()))
    y = solve(N, A)
    print('Case #{}: {}'.format(case, y))
