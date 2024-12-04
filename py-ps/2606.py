from collections import deque

N = int(input())
M = int(input())

path = [[False]*(N+1) for _ in range(N+1)]

def bfs(V):
    q = deque([V])
    visited[V] = True
    cnt = 0
    while q:
        V = q.popleft()
        for i in range(1, N+1) :
            if not visited[i] and path[V][i] :
                q.append(i)
                visited[i] = True
                cnt+=1
    print(cnt)


for _ in range(M) :
    a, b = map(int ,input().split())
    path[a][b] = True
    path[b][a] = True


visited = [False]*(N+1)

bfs(1)