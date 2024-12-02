from collections import deque

N, M, V = map(int, input().split())

path = [[False]*(N+1) for _ in range(N+1)]

for _ in range(M) :
    a, b = map(int ,input().split())
    path[a][b] = True
    path[b][a] = True

visited1 = [False]*(N+1)
visited2 = [False]*(N+1)

def bfs(V):
    q = deque([V])
    visited2[V] = True
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N+1) :
            if not visited2[i] and path[V][i] :
                q.append(i)
                visited2[i] = True

def dfs(V) :
    visited1[V] = True
    print(V, end=" ")
    for i in range(1, N+1) :
        if not visited1[i] and path[V][i] :
            dfs(i)


dfs(V)
print()
bfs(V)

