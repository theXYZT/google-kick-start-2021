# Kickstart 2021: Round B, Truck Delivery

import bisect
import math


def get_paths(graph):
    stack, visited, paths = [0], {0}, {0: []}
    while stack:
        v = stack[-1]
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                stack.append(w)
                paths[w] = paths[v][:]
                bisect.insort(paths[w], graph[w][v])
                break
        else:
            stack.pop()
    return paths


def solve_query(path, W):
    x = 0
    for L, A in path:
        if W < L:
            break
        x = math.gcd(x, A) if x else A
    return x


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N, Q = map(int, input().split())

    graph = [dict() for _ in range(N)]
    for _ in range(N - 1):
        X, Y, L, A = map(int, input().split())
        graph[X-1][Y-1] = graph[Y-1][X-1] = (L, A)

    paths = get_paths(graph)
    del graph

    y = []
    for _ in range(Q):
        C, W = map(int, input().split())
        y.append(solve_query(paths[C-1], W))

    print('Case #{}:'.format(case), *y)
