# 백준 12738번 가장 긴 증가하는 부분 수열 3
# GOLD 2
# 알고리즘 분류 : 이분 탐색, 가장 긴 증가하는 부분수열 : o(n log n)
import sys
input = sys.stdin.readline
A = int(input())
li = list(map(int,input().split()))
dp = [li[0]]
for i in range(1,A) :
    if li[i] > dp[-1] :
        dp.append(li[i])
        continue
    low = 0
    high = len(dp) - 1
    while low <= high :
        mid = (low+high)//2
        
        if dp[mid] >= li[i] :
            high = mid - 1
        else :
            low = mid + 1
    dp[low] = li[i]
print(len(dp))