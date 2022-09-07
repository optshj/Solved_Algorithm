# 백준 6549번 히스토그램에서 가장 큰 직사각형
# PLATINUM 5
# 알고리즘 분류 : 자료구조, 세그먼트 트리, 분할 정복, 스택
# 분할 정복 풀이
# 왼쪽에서의 넓이 오른쪽에서의 넓이 둘다 합친 것의 넓이중 가장 큰 것을 찾아서 출력
import sys
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
while True :
    li = list(map(int,sys.stdin.readline().split()))
    size = li.pop(0)
    if size == 0 :
        break
    print(max_area(0,size-1))