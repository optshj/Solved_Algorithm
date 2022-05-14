#2501번 약수 구하기
#BRONZE 3
a , b = map(int,input().split())
li = []
for i in range(1,a+1) :
    if a%i == 0 :
        li.append(i)
if b > len(li) :
    print(0)
else :
    print(li[b-1])