#6603¹ø ·Î¶Ç
#SILVER 2
import sys

def func(s,k) :
    if k == 6:
        print(' '.join(map(str,lst)))
        return

    for i in range(s,len(L)) :
        lst[k] = L[i]
        func(i+1,k+1)

while True :
    L = list(map(int,sys.stdin.readline().split()))
    if L[0] == 0 :
        break
    L.pop(0)
    lst = [0]*6
    func(0,0)
    print()