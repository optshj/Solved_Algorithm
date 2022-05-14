#2156번 포도주 시식
#SILVER 1
import sys
input = sys.stdin.readline
T = int(input())

li = [0]
for i in range(T):
    li.append(int(input()))
dp = [0]
dp.append(li[1])
if T > 1 :
    dp.append(li[2]+li[1])
for i in range(3,T+1): 
    dp.append(max(dp[i-3]+li[i-1]+li[i],dp[i-2]+li[i],dp[i-1]))
print(dp[T])