# 백준 2473번 세 용액
# GOLD 3
# 알고리즘 분류 : 정렬, 이분 탐색, 두 포인터
# low ~ N-1 까지 두 포인터로 mid,high를 고르면서 진행한다.
import sys
N = int(input())
li = list(map(int,input().split()))
li.sort()
ans = sys.maxsize
res = [0]*3
for low in range(N-2) :
    mid = low + 1
    high = N-1
    while mid < high :
        val = li[low] + li[mid] + li[high]
        if abs(val) < ans :
            ans = abs(val)
            res[0] = li[low]
            res[1] = li[mid]
            res[2] = li[high]
        if val < 0 :
            mid += 1
        else :
            high -= 1
print(*res)