#2455번 지능형 기차
#BRONZE 3
result = 0
li = []
for i in range(4) :
    a , b = map(int,input().split())
    result -= a
    li.append(result)
    result += b
    li.append(result)
print(max(li))