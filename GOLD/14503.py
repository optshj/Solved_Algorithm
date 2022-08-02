# 백준 14503번 로봇 청소기 
# GOLD 5
# 알고리즘 분류 : 구현, 시뮬레이션
# r,c 를 x,y로 변환할때 햇갈려서 삽질한 문제
# 간단한 dfs 탐색 문제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
r,c,d = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]

check[r][c] = 1
cnt = 1

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def dfs(x,y,d) :
    global cnt
    for i in range(4) :
        d_ = (d+3-i)%4
        x_ = x + dx[d_]
        y_ = y + dy[d_]
        if x_ < 0 or x_ > M-1 or y_ < 0 or y_ > N-1 :
            continue
        if li[y_][x_] == 0 and check[y_][x_] == 0 :
            check[y_][x_] = 1
            cnt += 1
            dfs(x_,y_,d_)

    x_ = x - dx[d]
    y_ = y - dy[d]
    if 0 <= x_ < M and 0 <= y_ < N :
        if li[y_][x_] == 0:
            dfs(x_,y_,d)
        else :
            print(cnt)
            exit()

dfs(c,r,d)