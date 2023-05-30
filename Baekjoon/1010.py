# input
tc = int(input())

# functions
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def bino_coef(n, r):
    # 동적 계획법
    cache = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    # 0개를 고르거나(r = 0), n과 r이 같은 경우는 그냥 1
    for i in range(n + 1):
        cache[i][0] = 1
    for i in range(r + 1):
        cache[i][i] = 1

    for i in range(1, n + 1):
        for j in range(1, r + 1):
            cache[i][j] = cache[i- 1][j] + cache[i - 1][j - 1]

    return cache[n][r]

# main
for i in range(tc):
    w, e = map(int, input().split())
    # print(factorial(e) // (factorial(w) * factorial(e - w)))
    print(bino_coef(e, w))
