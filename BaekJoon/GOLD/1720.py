# 백준 1720번 타일코드
# GOLD 4
# 알고리즘 분류 : 수학, 다이나믹 프로그래밍, 조합론
n = int(input())
dp = [0]*31
dp[0] = 1
dp[1] = 1
for i in range(2,n+1) :
    dp[i] = dp[i-1] + dp[i-2]*2
if n%2 :
  print((dp[n]+dp[(n-1)//2])//2)
else :
  print((dp[n] +dp[n//2]+dp[n//2-1]*2)//2)