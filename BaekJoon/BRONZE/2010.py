#2010번 플러그
#BRONZE 3
import sys
a = int(sys.stdin.readline())
li = []
for i in range(a) :
    li.append(int(sys.stdin.readline()))
print(sum(li)-a+1)