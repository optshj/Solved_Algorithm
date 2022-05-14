#1149¹ø RGB°Å¸®
#SILVER 1
import sys
N = int(sys.stdin.readline())
li = []
dp = [0]*(N-1)
for _ in range(N) :
    li.append(list(map(int,sys.stdin.readline().split())))
m = [0]*3
m[0] = min(li[0][1],li[0][2])+li[1][0]
m[1] = min(li[0][0],li[0][2])+li[1][1]
m[2] = min(li[0][0],li[0][1])+li[1][2]
dp[0] = m
for i in range(2,N) :
    m = [0]*3
    m[0] = min(dp[i-2][1],dp[i-2][2])+li[i][0]
    m[1] = min(dp[i-2][0],dp[i-2][2])+li[i][1]
    m[2] = min(dp[i-2][0],dp[i-2][1])+li[i][2]
    dp[i-1] = m
print(min(dp[-1]))