# 백준 1865번 웜홀
# GOLD 3
# 알고리즘 분류 : 그래프 이론, 벨만-포드
import sys

input = sys.stdin.readline
INF = sys.maxsize
TC = int(input())
ans = []
for _ in range(TC):
    N, M, W = map(int, input().split())
    dis = [INF] * (N + 1)
    g = []
    check = 0
    dis[1] = 0
    for i in range(M):
        S, E, T = map(int, input().split())
        g.append([S, E, T])
        g.append([E, S, T])
    for i in range(W):
        S, E, T = map(int, input().split())
        g.append([S, E, -T])
    for i in range(N):
        for j in range(2*M + W):
            cur = g[j][0]
            next_node = g[j][1]
            cost = g[j][2]
            if dis[next_node] > dis[cur] + cost:
                dis[next_node] = dis[cur] + cost
                if i == N - 1:
                    check = 1
    if check:
        ans.append("YES")
    else:
        ans.append("NO")
for _ in range(TC) :
  print(ans[_])
                  
