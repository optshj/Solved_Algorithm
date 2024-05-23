# 백준 1025번 제곱수 찾기
# GOLD 5
# 알고리즘 분류 : 브루트포스 알고리즘
N,M = map(int,input().split())
li = [list(input()) for _ in range(N)]
ans = []
def check(a) :
    if a == "" :
        return
    a = int(a)
    if a**0.5 == int(a**0.5) :
        ans.append(a)
for x_gap in range(-M,M) :
    for y_gap in range(-N,N) :
        if x_gap == 0 and y_gap == 0 :
            continue
        for start_x in range(M) :
            for start_y in range(N) :
                val = ""
                x = start_x
                y = start_y
                while 0 <= x < M and 0 <= y < N :
                    val += li[y][x]
                    x += x_gap
                    y += y_gap
                    check(val)
if ans :
    print(max(ans))
else :
    print(-1)