# 백준 13023번 ABCDE
# GOLD 5
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 깊이 우선 탐색
# 매분기마다 모든 경우를 탐색해야 되므로 한 줄기에서 탐색이 끝나면 방문 표시를 해제해주자.
import sys
input = sys.stdin.readline
def dfs(v,ans) :
    if ans == 4 :
        print(1)
        exit()
    check[v] = 1
    for i in g[v] :
        if not check[i] :
            dfs(i,ans+1)
            check[i] = 0
N,M = map(int,input().split())
g = [[] for _ in range(N)]
check = [0]*N
for _ in range(M) :
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(N) :
    dfs(i,0)
    check[i] = 0
print(0)