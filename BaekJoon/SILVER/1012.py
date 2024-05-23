# 백준 1012번 유기농 배추
# SILVER 2
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())

def dfs (x,y) :
    if x < 0 or x > N-1 or y < 0 or y > M-1 :
        return 0
    if g[x][y] :
        g[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return 1
    return 0

for _ in range(T) :
    M,N,K = map(int,input().split())
    cnt = 0
    g = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K) :
        a,b = map(int,input().split())
        g[b][a] = 1
    for i in range(N) :
        for j in range(M) :
            if dfs(i,j) :
                cnt += 1
    print(cnt)