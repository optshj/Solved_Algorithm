# 백준 1697번 숨바꼭질
# SILVER 1
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
# N에서 시작해서 K에 도착할때까지 bfs로 탐색하면서 이동횟수를 1씩 늘려줌 
# k에 도착하면 k번쨰 값을 반환
from collections import deque
N,K = map(int,input().split())
q = deque()
li = [0] * 100001
m = [1,-1,2]

def bfs(v) :
    q.append(v)
    while q :
        v = q.popleft()
        if v == K :
            return li[K]
        for i in range(3) :
            if i == 2 :
                v_ = v*2
            else :
                v_ = v + m[i]

            if 0 <= v_ < 100001 and not li[v_] :
                li[v_] = li[v] + 1
                q.append(v_)
print(bfs(N))