#2747�� �Ǻ���ġ ��
#BRONZE 3
a = int(input())
li = [0]*(a+1)
li[1] = 1
for i in range(2,a+1):
    li[i] = li[i-1] + li[i-2]
print(li[a])