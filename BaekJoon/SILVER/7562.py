# 백준 7562번 나이트의 이동
# SILVER 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque
input = sys.stdin.readline
move = [[2,1],[1,2],[2,-1],[1,-2],[-2,1],[-1,2],[-1,-2],[-2,-1]]
def bfs(x,y) :
    q.append((x,y))
    while q :
        x_,y_ = q.popleft()
        for _ in range(8) :
            m_x = x_ + move[_][0]
            m_y = y_ + move[_][1]
            if m_x < 0 or m_x > l-1 or m_y < 0 or m_y > l-1 :
                continue
            if g[m_x][m_y] == 0 :
                g[m_x][m_y] = g[x_][y_] + 1
                q.append((m_x,m_y))
            if m_x == x_m and m_y == y_m :
                print(g[x_m][y_m])
                return

T = int(input())
for _ in range(T) :
    l = int(input())
    q = deque()
    g = [[0 for i in range(l)] for i in range(l)]
    x,y = map(int,input().split())
    x_m,y_m = map(int,input().split())
    if x != x_m or y != y_m :
        bfs(x,y)
    else :
        print(0)