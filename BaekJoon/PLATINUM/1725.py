# 백준 1725번 히스토그램
# PLATINUM 5
# 알고리즘 분류 : 자료구조, 세그먼트 트리, 분할 정복, 스택
# 분할 정복 풀이
# 6549번이랑 똑같은 문제
import sys
input = sys.stdin.readline
def max_area(low,high) :
    if low == high :
        return li[low]
    mid = (low+high)//2
    height = min(li[mid],li[mid+1])
    val = max(max(max_area(low,mid),max_area(mid+1,high)),height*2)
    lo = mid
    hi = mid+1
    while lo > low or hi < high :
        if hi < high and (lo == low or li[hi+1] > li[lo-1]) :
            hi += 1
            height = min(height,li[hi])
        else :
            lo -= 1
            height = min(height,li[lo])
        val = max(val,height*(hi-lo+1))
    return val
N = int(input())
li = [int(input()) for _ in range(N)]
print(max_area(0,N-1))