#9461번 파도반 수열
#SILVER 3
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0]*N
    for i in range(0,N):
        if i == 0 or i == 1 or i == 2:
            dp[i] = 1
        elif i == 3 or i == 4:
            dp[i] = 2
        else :
            dp[i] = dp[i-1] + dp[i-5]
    print(dp[N-1])