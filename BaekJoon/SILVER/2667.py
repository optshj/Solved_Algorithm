# 백준 2667번 단지번호붙이기
# SILVER 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
sys.setrecursionlimit(10**6)
N = int(input())
def dfs(x,y) :
    global k
    if x < 0 or x > N-1 or y < 0 or y > N-1 :
        return 1
    if li[x][y] == '1' :
        li[x][y] = '0'
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        k += 1
        return 1
    return 0
li = [list(input()) for _ in range(N)]
k = 0
cnt = 0
res = []
for i in range(N) :
    for j in range(N) :
        if dfs(i,j) :
            res.append(k)
            k = 0
            cnt += 1
print(cnt)
print(*sorted(res),sep='\n')