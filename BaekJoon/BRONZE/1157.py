#1157 �ܾ� ����
#BRONZE 1
a = input()
a = a.upper()
li = []

for i in range(65,91) :
    li.append(a.count(chr(i)))

if li.count(max(li)) > 1 :
    print('?')
else :
    print(chr(li.index(max(li))+65))