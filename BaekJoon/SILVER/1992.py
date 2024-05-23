# 백준 19920번 쿼드트리
# SILVER 1
# 알고리즘 분류 : 이분 탐색, 매개 변수 탐색
# 메모리 30840KB, 시간 76ms ,언어 Python3 ,코드길이 :559B
import sys
input = sys.stdin.readline
N = int(input())
li = [list(input()) for _ in range(N)]
result = []
def check(N,v,h) :
    start = li[v][h]
    for i in range(h,h+N):
        for j in range(v,v+N) :
            if li[j][i] != start :
                return True
    result.append(start)
    return
def make(N,v,h) :
    if check(N,v,h) :
        result.append("(")
        make(N//2,v,h)
        make(N//2,v,h+N//2)
        make(N//2,v+N//2,h)
        make(N//2,v+N//2,h+N//2)
        result.append(")")
make(N,0,0)
for i in result :
    print(i,end='')