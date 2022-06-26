# 백준 2293번 동전 1
# GOLD 5
# 알고리즘 분류 : 다이나믹 프로그래밍
# 이전에 동전을 이용해 만든것의 합을 이용해서 dp에 저장한다.
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
li = [int(input()) for _ in range(N)]
dp = [0]*(K+1)
dp[0] = 1
for i in range(N) :
    for j in range(li[i],K+1) :
        dp[j] += dp[j-li[i]]
print(dp[-1])