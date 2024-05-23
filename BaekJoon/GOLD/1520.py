# 백준 1520번 내리막 길
# GOLD 3
# 알고리즘 분류 : 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 깊이 우선 탐색
import sys
sys.setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x,y) :
  if x == N-1 and y == M-1 :
    return 1
  if dp[y][x] != -1 :
    return dp[y][x]
  dp[y][x] = 0
  for i in range(4) :
    x_ = x + dx[i]
    y_ = y + dy[i]
    if x_ < 0 or x_ > N-1 or y_ < 0 or y_ > M-1 :
      continue
    if li[y_][x_] < li[y][x] :
      dp[y][x] += dfs(x_,y_)
  return dp[y][x]
input = sys.stdin.readline
M, N = map(int, input().split())
dp = [[-1] * (N + 1) for _ in range(M + 1)]
li = [list(map(int, input().split())) for _ in range(M)]
print(dfs(0,0))