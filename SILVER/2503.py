# 백준 2503번 숫자 야구
# SILVER 4
# 알고리즘 분류 : 구현, 브루트포스 알고리즘
# 메모리 : 30840KB, 시간 : 140ms, 언어 : Python3, 코드 길이 : 651B
import sys
input = sys.stdin.readline
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
for i in range(123,988) :
    a = str(i)
    if '0' in a :
        continue
    if len(set(a)) < 3 :
        continue
    check = 0
    for j in range(N) :
        b = str(li[j][0])
        cnt_ball = 0
        cnt_strike = 0
        for k in range(3) :
            if a[k] in b :
                cnt_ball += 1
            if b[k] == a[k] :
                cnt_strike += 1
                cnt_ball -= 1
        if cnt_strike != li[j][1] or cnt_ball != li[j][2] :
            check = 1
    if check == 0 :
        cnt += 1
print(cnt)