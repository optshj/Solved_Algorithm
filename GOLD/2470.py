# 백준 2470번 두 용액
# GOLD 5
# 알고리즘 분류 : 정렬, 이분 탐색, 두 포인터
# 내 풀이
import sys
N = int(input())
li = list(map(int,input().split()))
li.sort()
ans = [0]*2
min_val = sys.maxsize
low = 0
high = N - 1
while high > low :
    val = li[low] + li[high]
    if abs(val) < min_val :
        min_val = abs(val)
        ans[0] = li[low]
        ans[1] = li[high]
    if abs(li[low] + li[high-1]) > abs(li[low+1] + li[high]) :
        low += 1
    else :
        high -= 1
print(*ans)

#다른 풀이
import sys
N = int(input())
li = list(map(int,input().split()))
li.sort()
ans = [0]*2
min_val = sys.maxsize
low = 0
high = N - 1
while high > low :
    val = li[low] + li[high]
    if abs(val) < min_val :
        min_val = abs(val)
        ans[0] = li[low]
        ans[1] = li[high]
    if val < 0 :
        low += 1
    else :
        high -= 1
print(*ans)