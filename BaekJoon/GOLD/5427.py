# 백준 5427번 불
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# 어이없는 실수 하나때문에 오래걸린문제
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs() :
    q.append([a,b,0,0])
    while q :
        x,y,v,c = q.popleft()
        if c :
            for i in range(4) :
                x_ = x + dx[i]
                y_ = y + dy[i]
                if x_ < 0 or x_ > w-1 or y_ < 0 or y_ > h-1 :
                    continue
                if li[y_][x_] == '.' :
                    li[y_][x_] = '*'
                    q.append([x_,y_,v+1,1])

        else :
            if (x == 0 or x == w-1 or y == 0 or y == h-1) :
                return v+1
            for i in range(4) :
                x_ = x + dx[i]
                y_ = y + dy[i]
                if x_ < 0 or x_ > w-1 or y_ < 0 or y_ > h-1 :
                    continue
                if li[y_][x_] == '.' and not check[y_][x_] :
                    check[y_][x_] = 1
                    q.append([x_,y_,v+1,0])
    return 'IMPOSSIBLE'

for _ in range(T) :
    w,h = map(int,input().split())
    li = [list(input().rstrip()) for _ in range(h)]
    check = [[0]*w for i in range(h)]
    q = deque()
    for i in range(h) :
        for j in range(w) :
            if li[i][j] == '*' :
                q.append([j,i,0,1])
            if li[i][j] == '@' :
                check[i][j] = 1
                a,b = j,i
    print(bfs())