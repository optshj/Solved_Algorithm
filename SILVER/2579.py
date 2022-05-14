#2579번 계단 오르기
#SILVER 3
import sys
input = sys.stdin.readline
T = int(input())
li = []
dp = []
for n in range(T):
    li.append(int(input()))
    if n == 0 :
        dp.append(li[n])
        continue
    elif n == 1 :
        dp.append(max(li[n],dp[n-1]+li[n]))
        continue
    elif n == 2 :
        dp.append(max(dp[n-2]+li[n],li[n-1]+li[n]))
        continue
    dp.append(max(li[n]+li[n-1]+dp[n-3],li[n]+dp[n-2]))
print(dp[n])