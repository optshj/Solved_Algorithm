#1847번 스택 수열
#SILVER 3
import sys
input=sys.stdin.readline
a = int(input())
k = list(range(a,0,-1))
l = []
m = []
ca = 0
result = []
for _ in range(a):
    b = int(input())
    l.append(b)

for i in l :
    while True :
        if len(m)>0 and m[len(m)-1] == i :
            m.pop()
            result.append("-")
            break
        if k :
            m.append(k.pop())
            result.append("+")
        if m[len(m)-1] != i and len(k) == 0 :
            ca = 1
            break
        if m[len(m)-1] == i :
            m.pop()
            result.append("-")
            break

    
if ca == 0 :
    for i in result :
        print(i)
else :
    print("NO")