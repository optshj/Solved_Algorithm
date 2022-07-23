# 백준 1038번 감소하는 수
# GOLD 5
# 알고리즘 분류 : 브루트포스 알고리즘, 백트래킹
from itertools import combinations
N = int(input())
a = [0,1,2,3,4,5,6,7,8,9]
li = []
for i in range(1,11) :
    for j in combinations(a,i) :
        val = list(j)
        val.sort(reverse=True)
        li.append(int(''.join(list(map(str,val)))))
li.sort()
try :
    print(li[N])
except :
    print(-1)