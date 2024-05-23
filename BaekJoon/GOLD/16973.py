# 백준 16973번 직사각형 탈출
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 그레프 탐색, 너비 우선 탐색, 누적 합
from collections import deque
import sys

def bfs(r,c) :
    q = deque()
    q.append([r,c,0])
    check[r][c] = 1
    while q :
        r,c,v = q.popleft()
        if r == fr-1 and c == fc-1 :
            return v
        for i in range(4) :
            r_ = r + dr[i]
            c_ = c + dc[i]
            if r_ < 0 or r_ > N-H or c_ < 0 or c_ > M-W :
                continue
            flag = 0
            for wr,wc in wall :
                if r_ <= wr <= r_+H-1 and c_ <= wc <= c_+W-1 :
                    flag = 1
                    break
            if flag :
                continue
            if not check[r_][c_] :
                check[r_][c_] = 1
                q.append([r_,c_,v+1])
    return -1
dr = [1,-1,0,0]
dc = [0,0,1,-1]
input = sys.stdin.readline
N,M = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
wall = []
for i in range(N) :
    for j in range(M) :
        if li[i][j] :
            wall.append([i,j])
H,W,sr,sc,fr,fc = map(int,input().split())
check = [[0]*M for _ in range(N)]
print(bfs(sr-1,sc-1))