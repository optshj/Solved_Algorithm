#1904�� 01Ÿ��
#SILVER 3
import sys
N = int(sys.stdin.readline())
dp = [1,2]
for i in range(2,N):
    dp.append((dp[i-1]+dp[i-2])%15746)
print(dp[N-1])