#2751번 수 정렬하기 2
#SILVER 5
import sys
a = int(input())
li = []
for i in range(a) :
    li.append(int(sys.stdin.readline()))
li.sort()
for f in range(a) :
    print(li[f])