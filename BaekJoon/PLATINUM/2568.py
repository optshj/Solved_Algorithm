# 백준 2568번 전기줄 - 2
# PLATINUM 5
# 알고리즘 분류 : 가장 긴 증가하는 부분 수열: o(n log n)
# 2565번 전기줄 응용문제
# DP 트래킹과 이분 탐색을 이용한 DP 문제
import sys
input = sys.stdin.readline
N = int(input())
max_val = 0
li = []
check = [0]*500001
for i in range(N) :
    a,b = map(int,input().split())
    check[a] = 1
    li.append([a,b])
li.sort()
dp = [li[0][1]]
trace = [[0,li[0][0]]]
for i in range(1,N) :
    if li[i][1] > dp[-1] :
        dp.append(li[i][1])
        trace.append([len(dp)-1,li[i][0]])
    else :
        low = 0
        high = len(dp) - 1
        while low <= high :
            mid = (low+high)//2
            if dp[mid] >= li[i][1] :
                high = mid - 1
            else :
                low = mid + 1
        dp[low] = li[i][1]
        trace.append([low,li[i][0]])
temp = len(dp) - 1
ans = []
for i in range(N-1,-1,-1) :
    if trace[i][0] == temp :
        ans.append(trace[i][1])
        check[trace[i][1]] = 0
        temp -= 1
print(N - len(dp))
for i in range(500001) :
    if check[i] :
        print(i)