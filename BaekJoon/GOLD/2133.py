# 백준 2133번 타일 채우기
# GOLD 4
# 알고리즘 분류 : 다이나믹 프로그래밍
N = int(input())
dp = [0]*(31)
dp[0] = 1
dp[2] = 3
if N%2 :
  print(0)
else :
  for i in range(4,N+1) :
    dp[i] = dp[i-2]*dp[2]
    for j in range(0,i-3,2) :
      dp[i] += dp[j]*2
  print(dp[N])