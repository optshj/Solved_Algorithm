# 백준 13549번 숨바꼭질 3
# GOLD 5
# 알고리즘 분류 : 그래프, 0-1 너비 우선 탐색, 테이크스트라
# 단순 BFS인줄 알고 삽질을 했음. 
# https://www.acmicpc.net/board/view/38887
from collections import deque
N,K = map(int,input().split())
move = [2,-1,1]
li = [0]*100001
check = [0]*100001
def bfs(v) :
    q = deque()
    q.append(v)
    while q :
        v = q.popleft()
        if v == K :
            return li[v]
        for i in range(3) :
            if i == 0 :
                v_ = v*2
            else :
                v_ = v + move[i]
            if 0 <= v_ < 100001 and not check[v_] :
                check[v_] = 1
                if i == 0 :
                    li[v_] = li[v]
                else :
                    li[v_] = li[v] + 1
                q.append(v_)
print(bfs(N))