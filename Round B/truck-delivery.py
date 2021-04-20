# Kickstart 2021: Round B, Truck Delivery

import math


def query(C, W, path):
    x = 0
    for L, A in path:
        if L <= W:
            x = A
    return x


def update(prev, L, A):
    i, N = 0, len(prev)
    path = []
    if prev:
        while i < N and prev[i][0] < L:
            path.append(prev[i])
            i += 1

    A_new = math.gcd(path[-1][-1] if path else 0, A)
    if not path or path[-1][-1] != A_new:
        path.append((L, A_new))

    while i < N:
        A_next = math.gcd(prev[i][-1], A)
        if path[-1][-1] != A_next:
            path.append((prev[i][0], A_next))
        i += 1

    return path


def solve(N, Q, graph, queries):
    stack, found, paths = [0], {0}, {0: []}
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if w not in found:
                found.add(w)
                stack.append(w)
                paths[w] = update(paths[v], *graph[v][w])

    return [query(C, W, paths[C]) for C, W in queries]


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N, Q = map(int, input().split())

    graph = [dict() for _ in range(N)]
    for _ in range(N - 1):
        X, Y, L, A = map(int, input().split())
        graph[X-1][Y-1] = graph[Y-1][X-1] = (L, A)

    queries = []
    for i in range(Q):
        C, W = map(int, input().split())
        queries.append((C-1, W))

    y = solve(N, Q, graph, queries)
    print('Case #{}:'.format(case), *y)
