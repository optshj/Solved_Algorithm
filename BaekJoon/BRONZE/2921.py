#2921번 도미노
#BROZNE 3
a = int(input())
result = 0
for i in range(1,a+1):
    result += ((i)*(i+1)+i*(i+1)//2)
print(result)