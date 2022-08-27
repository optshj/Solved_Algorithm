# 백준 2550번 전구
# GOLD 3
# 알고리즘 분류 : 다이나믹 프로그래밍, 가징 긴 증가하는 부분 수열 : O(n log n)
# DP 길이를 구하는것은 쉬웠으나 DP 역추적을 몰라서 애먹은 문제
# 참조 : https://mygumi.tistory.com/303
N = int(input())
f = list(map(int,input().split()))
b = list(map(int,input().split()))
li = [0]*N
for i in range(N) :
    li[i] = b.index(f[i])
dp = []
trace = []
for i in range(N) :
    if len(dp) == 0 or li[i] > dp[-1] :
        dp.append(li[i])
        trace.append([len(dp)-1,li[i]])
        continue
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
    if temp == trace[i][0] :
        ans.append(b[trace[i][1]])
        temp -= 1
print(len(dp))
print(*sorted(ans))