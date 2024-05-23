# 백준 1759번 암호 만들기
# GOLD 5
# 알고리즘 분류 : 수학, 브루트포스 알고리즘, 조합론, 백트래킹
from itertools import combinations
L,C = map(int,input().split())
li = list(input().split())
check = list("aeiou")
vow = []
con = []
ans = []
for i in li :
    if i in check :
        vow.append(i)
    else :
        con.append(i)
for N in range(1,L-1) :
    for i in combinations(vow,N) :
        for j in combinations(con,L-N) :
            vow_li = list(map(str,i))
            con_li = list(map(str,j))
            val = vow_li + con_li
            val.sort()
            ans.append("".join(val))
ans.sort()
print(*ans,sep="\n")