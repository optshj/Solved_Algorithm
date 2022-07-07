# 백준 1504번 특정한 최단 경로
# GOLD 4
# 알고리즘 분류 : 그래프, 테이크스트라
# 1 -> v1 -> v2 -> N로 가는 경로와 1 -> v2 -> v1 -> N 로 가는 경우중 짧은 것을 출력
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

N,E = map(int,input().split())
w = [[] for _ in range(N+1)]

for _ in range(E) :
    a,b,c = map(int,input().split())
    w[a].append([b,c])
    w[b].append([a,c])
v1,v2 = map(int,input().split())

def shortest_path(s) :
    q = []
    heapq.heappush(q,[0,s])
    distance = [INF]*(N+1)
    distance[s] = 0
    while q :
        dist,now = heapq.heappop(q)
        if dist > distance[now] :
            continue
        for i in w[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])
    return distance

distance_1 = shortest_path(1)
distance_2 = shortest_path(v1)
distance_3 = shortest_path(v2)

c1 = distance_1[v1] + distance_2[v2] + distance_3[N]
c2 = distance_1[v2] + distance_3[v1] + distance_2[N]

ans = min(c1,c2)

if ans >= INF :
    print(-1)
else :
    print(ans)