#1978번 소수 찾기
#SILVER 4
import sys
def verf(i) :
    v = 2
    if i == 1 :
        return False
    while i >= v*v :
        if i%v == 0 :
            return False
        v += 1
    return True

a = int(input())
b = list(map(int,sys.stdin.readline().split()))
result = 0
for i in b :
    if verf(i):
        result += 1
print(result)
