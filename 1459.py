# 백준 1459번 걷기
# SILVER 5
# 알고리즘 분류 : 수학, 많은 조건 분기
# 메모리 : 30840 KB, 시간 : 72 ms, 언어 Python3, 코드길이 241B

X,Y,W,S = map(int,input().split())

min = min(X,Y)
gap = abs(X-Y)
c = gap%2
if 2*W < S :
    t = 2*W*min
else :
    t = S*min
if c == 0 and W > S :
    t += gap*S
elif c != 0 and W > S :
    t += (gap-c)*S + c*W
else :
    t += gap*W
print(t)