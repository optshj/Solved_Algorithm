#2477¹ø Âü¿Ü¹ç
#SILVER 4
import sys
input = sys.stdin.readline
K = int(input())
ver = []
hor = []
num = []
t = 1
for _ in range(6) :
    p,l = map(int,input().split())
    num.append(p)
    if p == 1 or p == 2 :
        hor.append(l)
    else :
        ver.append(l)
for i in range(-1,6) :
    if num[i-2] == 4 and num[i-1] == 1 and num[i] == 4 :
        t = 0
    elif num[i-2] == 3 and num[i-1] == 2 and num[i] == 3 :
        t = 0
if t :
    print(K*(max(ver)*max(hor)-ver[(ver.index(max(ver))-1)%3]*hor[(hor.index(max(hor))+1)%3]))
else :
    print(K*(max(ver)*max(hor)-ver[(ver.index(max(ver))+1)%3]*hor[(hor.index(max(hor))-1)%3]))