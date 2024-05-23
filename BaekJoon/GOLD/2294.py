# 백준 2294번 동전 2
# GOLD 5
# 알고리즘 분류 : 다이나믹 프로그래밍
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] + [10001] * k
for i in coins :
  for j in range(i,k+1) :
    dp[j] = min(dp[j],dp[j-i] + 1)
print(-1 if dp[k] == 10001 else dp[k])