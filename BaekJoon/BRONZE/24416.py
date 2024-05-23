# 백준 24416번 알고리즘 수업 - 피보나치 수 1
# BRONZE 1
# 알고리즘 분류 : 수학, 다이나믹 프로그래밍
N = int(input())
dp = [0]*(N+1)
dp[1] = 1
dp[2] = 1
for i in range(3,N+1) :
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N],end = ' ')
print(N-2)