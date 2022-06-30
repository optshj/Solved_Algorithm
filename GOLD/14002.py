# 백준 14002번 가장 긴 증가하는 부분 수열 4
# GOLD 4
# 알고리즘 분류 : 다이나믹 프로그래밍
import sys
input = sys.stdin.readline
A = int(input())
li = list(map(int,input().split()))
dp = [0]*(A+1)
res = []
for i in range(A) :
    for j in range(i) :
        if li[j] < li[i] :
            if dp[j+1] > dp[i+1] :
                dp[i+1] = dp[j+1]
    dp[i+1] += 1
print(max(dp))
idx = max(dp)
for i in range(A-1,-1,-1) :
    if dp[i+1] == idx :
        res.append(li[i])
        idx -= 1
print(*res[::-1])