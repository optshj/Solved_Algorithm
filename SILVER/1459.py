# 백준 1459번 걷기
# SILVER 5
# 알고리즘 분류 : 수학, 많은 조건 분기
# 메모리 : 30840 KB, 시간 : 72 ms, 언어 Python3, 코드길이 241B

X,Y,W,S = map(int,input().split())

min = min(X,Y)
gap = abs(X-Y)
c = gap%2

# 대각으로 한번에 가는 것이 한 블록을 두번 걸을때 보다 빠를 
if 2*W < S :
    t = 2*W*min
else :
    t = S*min

# 대각으로 두번 / \ 처럼 이동하면 가로 또는 세로로 두칸 이동 할 수 있음
# 대각으로 두번 이동할때가 가로 세로로 두번 이동하는 것 보다 빠른 경우
if c == 0 and W > S :
    t += gap*S
elif c != 0 and W > S :
    t += (gap-c)*S + c*W
else :
    t += gap*W
print(t)