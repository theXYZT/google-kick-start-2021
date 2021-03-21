# Kickstart 2021: Round A, K-Goodness String


def min_operations(N, K, S):
    goodness = 0
    for i in range(N//2):
        a, b = S[i], S[-i-1]
        goodness += (a != b)
    return abs(K - goodness)


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N, K = map(int, input().split())
    S = input().strip()
    y = min_operations(N, K, S)
    print('Case #{}: {}'.format(case, y))
