# main
count = 1
while True:
    n = int(input())
    if n == 0:
        break
    name_arr = [input() for _ in range(n)]
    info = [input().split() for _ in range(2*n - 1)]

    check_arr = [0 for _ in range(n)]
    for s in info:
        check_arr[int(s[0]) - 1] += 1

    girl_idx = check_arr.index(1)

    print(str(count) + ' ' + name_arr[girl_idx])
    count += 1

