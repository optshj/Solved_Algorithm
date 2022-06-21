# 백준 2664번 촌수계산
# SILVER 2
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
N = int(input())
a,b = map(int,input().split())
m = int(input())
g = [[0] for _ in range(N+1)]
check = [0]*(N+1)
for i in range(m) :
    x,y = map(int,input().split())
    g[x].append(y)
    g[y].append(x)
ans = -1

def dfs(v,a) :
    if v == b:
        global ans
        ans = a 
        return
    check[v] = 1
    for i in g[v] :
        if check[i] == 0 :
            dfs(i,a+1)
dfs(a,0)
print(ans)