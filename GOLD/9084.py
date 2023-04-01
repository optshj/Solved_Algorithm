# 백준 9084번 동전
# GOLD 5
# 알고리즘 분류 : 다이나믹 프로그래밍, 배낭 문제
T = int(input())
for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M + 1)
    dp[0] = 1
    for i in range(N):
        for j in range(coin[i], M + 1):
                dp[j] += dp[j - coin[i]]
    print(dp[-1])
