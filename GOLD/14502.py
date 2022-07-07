# 백준 14502번 연구소
# GOLD 5
# 알고리즘 분류 : 그래프, 브루트포스 알고리즘, 너비 우선 탐색
import sys
import copy
from collections import deque
N,M = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
max_val = 0
def bfs() :
    q = deque()
    cnt = 0
    check = [[0]*M for _ in range(N)]
    for x in range(M) :
        for y in range(N) :
            if li[y][x] == 2 :
                q.append([x,y])
                check[y][x] = 1
    while q :
        x,y = q.popleft()
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > M-1 or y_ < 0 or y_ > N-1 :
                continue
            if li[y_][x_] == 0 and not check[y_][x_]:
                li[y_][x_] = 2
                check[y_][x_] = 1
                q.append([x_,y_])
    for i in range(N) :
        cnt += li[i].count(0)
    return cnt

for x1 in range(M) :
    for y1 in range(N) :
        if li[y1][x1] == 0 :
            li[y1][x1] = 1 
            for x2 in range(M) :
                for y2 in range(N) :
                    if li[y2][x2] == 0 :
                        li[y2][x2] = 1
                        for x3 in range(M):
                            for y3 in range(N) :
                                if li[y3][x3] == 0:
                                    copy_list = copy.deepcopy(li)
                                    li[y3][x3] = 1
                                    cnt_val = bfs()
                                    max_val = max(cnt_val,max_val)
                                    li = copy.deepcopy(copy_list)
                                    li[y3][x3] = 0
                        li[y2][x2] = 0
            li[y1][x1] =0
print(max_val)