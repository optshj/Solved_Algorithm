# 백준 1780번 종이의 개수
# SILVER 2
# 알고리즘 분류 : 분할 정복, 재귀
# 메모리 68852KB, 시간 3092ms ,언어 Python3 ,코드길이 :777B
import sys
input = sys.stdin.readline
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
result = [0]*3
def check(N,v,h) :
    start = li[v][h]
    for i in range(h,h+N):
        for j in range(v,v+N) :
            if li[j][i] != start :
                return True
    result[start] += 1
    return
def make(N,v,h) :
    if N == 1 :
        result[li[v][h]] += 1
        return
    if check(N,v,h) :
        make(N//3,v,h)
        make(N//3,v+N//3,h)
        make(N//3,v+2*(N//3),h)
        make(N//3,v,h+N//3)
        make(N//3,v,h+2*(N//3))
        make(N//3,v+N//3,h+N//3)
        make(N//3,v+2*(N//3),h+2*(N//3))
        make(N//3,v+N//3,h+2*(N//3))
        make(N//3,v+2*(N//3),h+N//3)
make(N,0,0)
print(result[-1])
print(result[0])
print(result[1])