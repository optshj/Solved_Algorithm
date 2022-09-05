# 백준 14226번 이모티콘
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque
def bfs() :
    q = deque()
    q.append([1,0,0])
    check[1][0] = 1
    while q :
        v,c,m = q.popleft()
        if v == S :
            return m
        if not check[v][v] :
            q.append([v,v,m+1])
            check[v][v] = 1
        if v+c < 1001 and not check[v+c][c] :
            q.append([v+c,c,m+1])
            check[v+c][c] = 1
        if v-1 >= 0 and not check[v-1][c] :
            q.append([v-1,c,m+1])
            check[v-1][c] = 1
        

S = int(input())
check = [[0]*1001 for _ in range(1001)]
print(bfs())