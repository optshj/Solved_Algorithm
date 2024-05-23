# 백준 2583번 영역 구하기
# SILVER 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
M,N,K = map(int,input().split())
k = 0
cnt = 0
g = [[0]*(N) for _ in range(M)]
ans = []
for _ in range(K) :
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2) :
        for j in range(y1,y2) :
            g[j][i] = 1
def dfs(x,y) :
    global k
    if x < 0 or x > M-1 or y < 0 or y > N-1 :
        return 1
    if g[x][y] == 0 :
        g[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        k += 1
        return 1
    return 0
for i in range(M) :
    for j in range(N) :
        if dfs(i,j) :
            ans.append(k)
            k = 0
            cnt += 1
print(cnt)
print(*sorted(ans))