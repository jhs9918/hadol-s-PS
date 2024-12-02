a, p = map(int, input().split())
cnt = 1

graph = [0]*250000

def pows(n, p):
    ans = 0
    while n > 0:
        ans += pow(n % 10, p) 
        n //= 10  
    return ans 

def dfs(a, p, graph, cnt) :
    if graph[a] != 0 :
        return graph[a]-1
    nst = pows(a, p)
    graph[a] = cnt
    cnt+=1
    return dfs(nst, p, graph, cnt)

print(dfs(a, p, graph, cnt))