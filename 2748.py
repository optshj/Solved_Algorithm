#2748번 피보나치 수 2
#BRONZE 1
a = int(input())
li = [0]*(a+1)
li[1] = 1
for i in range(2,a+1) :
    li[i] = li[i-1] + li[i-2]
print(li[a])