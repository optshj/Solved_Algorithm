# 백준 1377번 버블 소트
# GOLD 2
# 알고리즘 분류 : 정렬
# 메모리 : 107488KB, 시간 : 1808ms, 언어 : Python3, 코드 길이 : 177B
import sys
input = sys.stdin.readline
N = int(input())
li = [[int(input()),_] for _ in range(N)]
li.sort()
cnt = 0
for i in range(N) :
    cnt = max(cnt,li[i][1]-i)
print(cnt+1)