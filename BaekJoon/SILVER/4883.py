# 백준 4833번 삼각 그래프
# SILVER 1
# 알고리즘 분류 : 다이나믹 프로그래밍
import sys
input = sys.stdin.readline
case = 0
while True :
  T = int(input())
  case += 1
  if T == 0 :
    break
  li = [list(map(int,input().split())) for _ in range(T)]
  dp = [[0]*3 for _ in range(T)]
  dp[0][0] = li[0][1]
  dp[0][1] = li[0][1]
  dp[0][2] = li[0][1] + li[0][2]
  for i in range(1,T) :
    dp[i][0] = min(dp[i-1][0],dp[i-1][1]) + li[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][1],dp[i-1][2],dp[i][0]) + li[i][1]
    dp[i][2] = min(dp[i-1][1],dp[i-1][2],dp[i][1]) + li[i][2]
  print(f"{case}. {dp[-1][1]}")
      