#2506번 점수계산
#BRONZE 3
a = int(input())
b = list(map(int,input().split()))
result = 0
k = 0
for i in b :
    if i == 1 :
        k += 1
        result += k
    elif i == 0 :
        k = 0
print(result)