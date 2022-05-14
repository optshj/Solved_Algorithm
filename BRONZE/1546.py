#1546¹ø Æò±Õ
#BRONZE 1
a = int(input())
li = list(map(int,input().split()))
b = max(li)
result = 0
for i in range(0,a) :
    result += li[i]/b*100
print(result/a)