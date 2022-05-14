#1699번 제곱수의 합
#SILVER 3
import math
N = int(input())
dp = [0]
li = [i**2 for i in range(0,int(math.sqrt(N)))]
for i in range(1,N+1) :
    if i in li :
        dp.append(1)
        continue
    min_val = 10000000
    for j in range(1,int(math.sqrt(i))+1) :
        if min_val > dp[i-j**2]:
            min_val = dp[i-j**2]
    dp.append(min_val + 1)
print(dp[N])