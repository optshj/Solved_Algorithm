# 백준 1107번 리모콘
# GOLD 5
# 알고리즘 분류 : 브루트포스 알고리즘
from itertools import product
N = input()
len_N = len(N)
N = int(N)
M = int(input())
min_val = abs(N-100)
if M == 0 :
    print(min(abs(N-100),len_N))
    exit()
vec = [0,1,2,3,4,5,6,7,8,9]
li = list(map(int,input().split()))


for i in range(M) :
    vec.remove(li[i])
for j in range(1,len_N+2) :
    for i in product(vec,repeat=j) :
        val = list(i)
        val = int("".join(list(map(str,val))))
        min_val = min(min_val,abs(val-N)+j)
print(min_val)

# 다른 풀이
N = int(input())
M = int(input())
min_val = abs(N-100)
if M == 0 :
    li = []
else :
    li = list(map(int,input().split()))


for i in range(1000000) :
    for j in str(i) :
        if int(j) in li :
            break
    else :
        min_val = min(min_val,len(str(i)) + abs(N-i))
print(min_val)