# Kickstart 2021: Round B, Increasing Substring


def solve(N, S):
    y = [1, ]
    prev = 0
    for i in range(1, N):
        if S[i] <= S[i-1]:
            prev = i
        y.append(i - prev + 1)
    return y


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input().strip())
    S = input().strip()
    y = solve(N, S)
    print('Case #{}:'.format(case), *y)
