#2485�� ���μ�
#SILVER 4
import sys

def gcd(a,b):
    while b > 0:
        a,b = b,a%b

    return a

input = sys.stdin.readline
T = int(input())
li = []
a = int(input())

for _ in range(T-1):
    k = int(input())
    li.append(k-a)
k = []
for i in range(0,len(li)-1):
    k.append(gcd(li[i],li[i+1]))
print((li[len(li)-1]//min(k))-len(li))