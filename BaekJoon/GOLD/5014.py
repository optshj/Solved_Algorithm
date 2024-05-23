# 백준 5014번 스타트링크
# GOLD 5
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
from collections import deque
F,S,G,U,D = map(int,input().split())
move = [U,-D]
check = [0]*(F+1)
def bfs(v) :
    q = deque()
    q.append([v,0])
    check[v] = 1
    while q :
        v,m = q.popleft()
        if v == G :
            return m
        for i in range(2) :
            v_ = v + move[i]
            if v_ > F or v_ <= 0 :
                continue
            if not check[v_] :
                q.append([v_,m+1])
                check[v_] = 1
val = bfs(S)
if val != None :
    print(val)
else :
    print("use the stairs")