# 백준 25326번 다중 항목 선호도 조사 (Small)
# BRONZE 1
# 알고리즘 분류 : 브루트포스 알고리즘
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
li = [list(map(str,input().split())) for _ in range(N)]
for _ in range(M) :
    cnt = 0
    ans = list(map(str,input().split()))
    for i in range(N) :
        if (ans[0] == '-' or li[i][0] == ans[0]) and (ans[1] == '-' or li[i][1] == ans[1]) and (ans[2] == '-' or li[i][2] == ans[2]) :
            cnt += 1
    print(cnt)