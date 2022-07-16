# 백준 1956번 운동
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 플로이드-워셜
import sys
INF = sys.maxsize
V,E = map(int,input().split())
g = [[INF]*(V+1) for _ in range(V+1)]
ans = INF
for _ in range(E) :
    a,b,w = map(int,input().split())
    g[a][b] = min(w,g[a][b])
for k in range(V+1) :
    for i in range(V+1) :
        for j in range(V+1) :
            g[i][j] = min(g[i][k] + g[k][j],g[i][j])
for i in range(V) :
    ans = min(ans,g[i][i])
print(ans if ans != INF else -1)