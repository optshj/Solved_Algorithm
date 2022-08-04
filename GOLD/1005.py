# 백준 1005번 ACM Craft
# GOLD 3
# 알고리즘 분류 : 다이나믹 프로그래밍, 그래프 이론, 위상 정렬
# 위상 정렬 활용 문제 해당 노드까지 걸리는 시간을 DP로 저장하고 다른 노선에서 오는 경우가 있으면 비교를 해 큰 값을 저장
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    N,K = map(int,input().split())
    li = [0] + list(map(int,input().split()))
    g = [[] for i in range(N+1)]
    indegree = [0]*(N+1)
    ans = 0
    q = deque()
    for i in range(K) :
        a,b = map(int,input().split())
        g[a].append(b)
        indegree[b] += 1
    W = int(input())
    time = [0]*(N+1)
    for i in range(1,N+1) :
        if indegree[i] == 0 :
            q.append(i)
            time[i] = li[i]
    while q :
        now = q.popleft()
        for i in g[now] :
            indegree[i] -= 1
            time[i] = max(time[i],li[i]+time[now])
            if indegree[i] == 0 :
                q.append(i)
    print(time[W])