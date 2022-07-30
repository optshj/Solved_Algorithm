# 백준 2573번 빙산
# GOLD 4
# 알고리즘 분류 : 구현, 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 너비 우선 탐색
# 메모리초과가 날땐 순환 횟수를 줄여보자
# 파이썬은 BFS가 DFS보다 빠른것 같다 ?
# BFS : 912 ms DFS : 1656 ms
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
ans = 0

sys.setrecursionlimit(100000)
def dfs(x,y) :
    if x < 0 or x > M-1 or y < 0 or y > N-1 :
        return
    if li[y][x] and not check[y][x]:
        check[y][x] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y) : 
    q = deque()
    q.append([x,y])
    while q :
        x,y = q.popleft()
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > M-1 or y_ < 0 or y_ > N-1 :
                continue
            if li[y_][x_] and not check[y_][x_] :
                check[y_][x_] = 1
                q.append([x_,y_])
def water(x,y) :
    if x < 0 or x > M-1 or y < 0 or y > N-1 :
        return
    if li[y][x] != 0 :
        li[y][x] -= 1


while True :
    check = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(M) :
        for j in range(N) :
            if li[j][i] and not check[j][i] :
                bfs(i,j)
                cnt += 1
    if cnt >= 2 :
        print(ans)
        break
    elif cnt == 0 :
        print(0)
        break
    for i in range(M) :
        for j in range(N) :
            if check[j][i] == 0 :
                water(i-1,j)
                water(i+1,j)
                water(i,j-1)
                water(i,j+1)
    ans += 1