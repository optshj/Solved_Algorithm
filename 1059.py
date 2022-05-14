#1059번 좋은 구간
#SILVER 5
L = int(input())
S = list(map(int,input().split()))
S.sort()
n = int(input())
for i in range(L) :
    if n < S[i] :
        break
if n in S :
    print(0)
elif i == 0 :
    print(n*(S[i]-n)-1)
else :
    print((S[i] - n)*(n - S[i-1])-1)