#2476번 주사위 게임
#BRONZE 3
a = int(input())
result = []
for i in range(a):
    A,B,C = map(int,input().split())
    cnt = [A,B,C]

    cnt = sorted(cnt)
    if A == B and B == C :
        result.append(10000 + A*1000)
    elif A != B and B != C and C != A :
        result.append(max(cnt)*100)
    else :
        result.append(1000+ cnt[1]*100)

print(max(result))