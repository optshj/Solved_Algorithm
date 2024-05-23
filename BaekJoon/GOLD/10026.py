# 백준 10026번 적록색약
# GOLD 5
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
li = [list(input()) for _ in range(N)]
check = copy.deepcopy(li)
cnt_nom = 0
cnt_weak = 0

def dfs(x,y,c) :
    if (0 <= x < N) and (0 <= y < N) :
        if li[x][y] == c :
            li[x][y] = 0
            dfs(x-1,y,c)
            dfs(x+1,y,c)
            dfs(x,y-1,c)
            dfs(x,y+1,c)
for i in range(N) :
    for j in range(N) :
        if li[i][j] != 0 :
            dfs(i,j,li[i][j])
            cnt_nom += 1
li = check
for i in range(N) :
    for j in range(N) :
        if li[i][j] == 'R' :
            li[i][j] = 'G'
for i in range(N) :
    for j in range(N) :
        if li[i][j] != 0 :
            dfs(i,j,li[i][j])
            cnt_weak += 1
print(cnt_nom,cnt_weak)