#1929번 소수 구하기
#SILVER 3
import sys
def verf(i) :
    v = 2
    while i >= v*v :
        if i%v == 0 :
            return False
        v += 1
    return True

M,N = map(int,sys.stdin.readline().split())
li = list(range(0,N+1))
li[1] = 0
i = 2
while i*i< N+1 :
    if li[i] != 0 and verf(li[i]) :
        for j in range(i*2,N+1,i) :
            li[j] = 0
    i += 1
for k in range(M,N+1) :
    if li[k] != 0 :
        print(k)
