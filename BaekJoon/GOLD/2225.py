# 백준 2225번 합분해
# GOLD 5
# 알고리즘 분류 : 수학, 다이나믹 프로그래밍
N,K = map(int,input().split())
dp = [[0]*(N+1) for _ in range(K+1)]
for i in range(N+1) :
  dp[1][i] = 1
for i in range(1,K+1) :
  for j in range(N+1) :
    for k in range(j+1) :
      dp[i][j] += (dp[i-1][j-k])%1000000000
print(dp[-1][-1]%1000000000)