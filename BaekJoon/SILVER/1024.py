# 백준 1024번 수열의 합
# SILVER 2
# 알고리즘 분류 : 수학
# 수열의 합의 성질을 이용해서 푸는 문제
N,L = map(int,input().split())
for i in range(L,101) :
    x = N - (i**2+i)//2
    if x%i == 0 and x//i + 1 >= 0 :
        x = x//i
        print(*[i for i in range(x+1,x+i+1)])
        exit()
print(-1)