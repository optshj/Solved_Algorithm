#1292�� ���� Ǫ�� ����
#SILVER 5
A,B = map(int,input().split())
li = []
for i in range(1,46) :
    for j in range(i) :
        li.append(i)
print(sum(li[A-1:B]))