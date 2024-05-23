# 백준 2617번 구슬 찾기
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 플로이드-워셜
# DFS로 자기보다 크거나 작은게 몇개인지 세고 갯수가 과반수가 넘으면 중간은 절대 될 수 없다.
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
N,M = map(int,input().split())
light_g = [[] for _ in range(N+1)]
heavy_g = [[] for _ in range(N+1)]
ans = 0
def light_dfs(v) :
    global cnt1
    check_light[v] = 1
    for i in light_g[v] :
        if not check_light[i] :
            cnt1 += 1
            light_dfs(i)
def heavy_dfs(v) :
    global cnt2
    check_heavy[v] = 1
    for i in heavy_g[v] :
        if not check_heavy[i] :
            cnt2 += 1
            heavy_dfs(i)
for _ in range(M) :
    a,b = map(int,input().split())
    light_g[a].append(b)
    heavy_g[b].append(a)
for i in range(1,N+1) :
    check_light = [0]*(N+1)
    check_heavy = [0]*(N+1)
    cnt1 = 0
    cnt2 = 0
    light_dfs(i)
    heavy_dfs(i)
    if cnt1 >= (N+1)/2 or cnt2 >= (N+1)/2 :
        ans += 1
print(ans)
