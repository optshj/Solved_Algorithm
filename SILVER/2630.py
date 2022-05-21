# 백준 2330번 색종이 만들기
# SILVER 3
# 알고리즘 분류 : 분할 정복, 재귀
# 메모리 30840KB, 시간 96ms ,언어 Pythone3 ,코드길이 :684B
import sys
input = sys.stdin.readline
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
result =[0]*2
def check(N,v,h) :
    start = li[v][h]
    k = 0
    for i in range(v,v+N) :
        for j in range(h,h+N) :
            if start != li[i][j] :
                k = 1
    if k :
        return 0
    elif start == 0 :
        return 2
    return 1
def make(N,v,h) :
    k = check(N,v,h)
    if k == 0 :
        make(N//2,v,h)
        make(N//2,v,h+N//2)
        make(N//2,v+N//2,h)
        make(N//2,v+N//2,h+N//2)
    else :
        if k == 1 :
            result[0] += 1
        else :
            result[1] += 1
make(N,0,0)
print(result[1])
print(result[0])