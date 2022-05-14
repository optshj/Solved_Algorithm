#1977번 완전제곱수
#BRONZE 1
M = int(input())
N = int(input())
sum = 0
min = 0
for i in range(M,N+1) :
    if i**0.5 - int(i**0.5) == 0 :
        sum += i
        if min == 0 :
            min = i
        elif min > i :
            min = i
if sum == 0 :
    print(-1)
else :
    print(sum)
    print(min)