# 백준 14003번 가장 긴 증가하는 부분 수열 5
# PLATINUM 5
# 알고리즘 분류 : 이분 탐색, 가장 긴 증가하는 부분 수열 O(n log n)
N = int(input())
li = list(map(int,input().split()))
dp = [li[0]]
trace = [[0,li[0]]]
for i in range(1,N) :
    if li[i] > dp[-1] :
        dp.append(li[i])
        trace.append([len(dp)-1,li[i]])
    else :
        low = 0
        high = len(dp) - 1
        while low <= high :
            mid = (low+high)//2

            if dp[mid] >= li[i] :
                high = mid - 1
            else :
                low = mid + 1
        trace.append([low,li[i]])
        dp[low] = li[i]
ans = []
temp = len(dp) - 1
for i in range(N-1,-1,-1) :
    if trace[i][0] == temp :
        ans.append(trace[i][1])
        temp -= 1
print(len(dp))
ans.reverse()
print(*ans)
