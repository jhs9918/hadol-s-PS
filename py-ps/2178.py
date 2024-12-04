from collections import deque

n, m = map(int, input().split())

dx = (1, 0 , -1, 0)
dy = (0, 1, 0 , -1)

node = []

for _ in range(n) :
    node.append([int(char) for char in input()])

q = deque()

q.append((0,0))

while q :
    x, y = q.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or ny<0 or nx >= n or ny >= m or node[nx][ny] == 0  :
            continue
        
        if node[nx][ny] == 1:
            node[nx][ny] = node[x][y] + 1
            q.append((nx,ny))

print(node[n-1][m-1])