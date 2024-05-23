#2193번 이친수
#SILVER 3
a = int(input())
dp = [1,1]
for i in range(2,a):
    dp.append(dp[i-2]+dp[i-1])
print(dp[a-1])