# input
k_visited = []
for i in range(36):
    k_visited.append(list(input()))
k_visited.append(k_visited[0])

col = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}
row = {'1':5, '2':4, '3':3, '4':2, '5':1, '6':0}
dx = [-2, -2, 1, -1, 2, 2, 1, -1]
dy = [1, -1, 2, 2, 1, -1, -2, -2]

# function
def checkMove(x1, y1, x2, y2):
    if visited[x2][y2]:
        return False
    for d in range(8):
        nx = x1 + dx[d]
        ny = y1 + dy[d]
        if 0 <= nx < 6 and 0 <= ny < 6 and (nx, ny) == (x2, y2):
            visited[nx][ny] = True
            return True
    return False


# main
visited = [[False] * 6 for _ in range(6)]
for i in range(36):
    x1, y1 = row[k_visited[i][1]], col[k_visited[i][0]]
    x2, y2 = row[k_visited[i+1][1]], col[k_visited[i+1][0]]
    if not checkMove(x1, y1, x2, y2):
        print('Invalid')
        break
else:
    print('Valid')