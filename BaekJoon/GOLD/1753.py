# 백준 1753번 최단경로
# GOLD 4
# 알고리즘 분류 : 그래프, 테이크스트라
# 우선순위 큐를 이용해 choose를 대체하는 식의 풀이 우선순위 큐를 사용하지 않으면 시간초과
# 첫번쨰 풀이(우선순위 큐 x)
import sys
input = sys.stdin.readline

INF = sys.maxsize

V,E = map(int,input().split())
s = int(input())
weight = [[] for _ in range(V+1)]
distance = [INF]*(V+1)
visited = [0]*(V+1)

for _ in range(E) :
    a,b,w = map(int,input().split())
    weight[a].append([b,w])

def choose() :
    min_value = INF
    idx = 0
    for i in range(1,V+1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            idx = i
    return idx

def shortest_path(s) :
    distance[s] = 0
    visited[s] = 1
    for i in weight[s] :
        if distance[i[0]] >= i[1] :
            distance[i[0]] = i[1]

    for i in range(V-1) :
        now = choose()
        visited[now] = 1
        for j in weight[now] :
            cost = distance[now] + j[1]
            if cost < distance[j[0]] :
                distance[j[0]] = cost

shortest_path(s)

for i in distance[1:] :
    if i == INF :
        print('INF')
    else :
        print(i)
        
# 두번쨰 풀이 (우선순위 큐 o)
import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize

V,E = map(int,input().split())
s = int(input())
weight = [[] for _ in range(V+1)]
distance = [INF]*(V+1)
visited = [0]*(V+1)

for _ in range(E) :
    a,b,w = map(int,input().split())
    weight[a].append([b,w])


def shortest_path(s) :
    q = []
    heapq.heappush(q,[0,s])
    distance[s] = 0
    while q :
        dist,now = heapq.heappop(q)
        if dist > distance[now] or visited[now]:
            continue
        visited[now] = 1
        for i in weight[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])

shortest_path(s)
for i in distance[1:] :
    if i == INF :
        print('INF')
    else :
        print(i)