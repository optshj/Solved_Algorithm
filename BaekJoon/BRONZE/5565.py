#5565�� ������
#BRONZE 3
import sys
a = int(sys.stdin.readline())
li = []
for i in range(9) :
    b = int(sys.stdin.readline())
    li.append(b)
print(a-sum(li))