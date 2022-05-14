#5543번 상근날드
#BROZNE 4
li1 = []
li2 = []
for i in range(5):
    if i <3 :
        li1.append(int(input()))
    else :
        li2.append(int(input()))
print(min(li1)+min(li2)-50)