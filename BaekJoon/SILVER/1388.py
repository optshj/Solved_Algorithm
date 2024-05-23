# 백준 1388번 바닥 장식
# SILVER 4
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# 메모리 : 30840KB, 시간 : 76ms, 언어 : Python3, 코드 길이 : 523B
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
li = [list(input()) for _ in range(N)]
cnt = 0
for i in range(N) :
    k = 1
    for j in range(M) :
        if li[i][j] == '-' :
            if k == 1 :
                cnt += 1
            k = 0
        elif li[i][j] == '|' :
            k = 1
for i in range(M) :
    k = 1
    for j in range(N) :
        if li[j][i] == '|' :
            if k == 1:
                cnt += 1
            k = 0
        elif li[j][i] == '-' :
            k = 1
print(cnt)