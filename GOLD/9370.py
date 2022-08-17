# 백준 9370번 미확인 도착지
# GOLD 2
# 알고리즘 분류 : 그래프 이론, 데이크스트라
# S->G->H->E 또는 S->H->G->E 로 가는 길이가 S->E로 가는 길이와 같은 경우 정답
import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

T = int(input())
def shortest_path(start) :
    q = []
    heapq.heappush(q,[0,start])
    distance = [INF]*(n+1)
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now] :
            continue
        for i in w[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])
    return distance

for _ in range(T) :
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    w = [[] for _ in range(n+1)]
    
    for i in range(m) :
        a,b,d = map(int,input().split())
        w[a].append([b,d])
        w[b].append([a,d])
    path_s = shortest_path(s)
    path_g = shortest_path(g)
    path_h = shortest_path(h)

    ans = []
    for _ in range(t) :
        e = int(input())
        if (path_s[g]+path_g[h]+path_h[e] == path_s[e]) or (path_s[h]+path_h[g]+path_g[e] == path_s[e]) :
            ans.append(e)
    ans.sort()
    print(*ans)
