#2480번 주사위 세개
#BRONZE 4
A,B,C = map(int,input().split())
li = [A,B,C]
li = sorted(li)
if A == B and B == C :
    print(10000+A*1000)
elif A != B and B != C and A != C :
    print(max(li)*100)
else :
    print(1000+li[1]*100)
