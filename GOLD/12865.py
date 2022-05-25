# 백준 12865번 평범한 배낭
# GOLD 5
# 알고리즘 분류 : 다이나믹 프로그래밍, 배낭 문제
# 메모리 192888KB, 시간 344ms ,언어 PyPy3 ,코드길이 :344B
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
dp = [[0 for i in range(K+1)] for _ in range(N)]
for i in range(0,N) :
    w,v = map(int,input().split())
    for j in range(1,K+1) :
        if j >= w :
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
        else :
            dp[i][j] = dp[i-1][j]
print(max(dp[-1]))