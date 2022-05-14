#5622번 다이얼
#BRONZE 2
b = list(input())
cn = 0
for i in b :
    if i == 'A' or i == 'B' or i =='C' :
        cn += 3
    elif i == 'D' or i == 'E' or i =='F' :
        cn += 4
    elif i == 'G' or i == 'H' or i =='I' :
        cn += 5
    elif i == 'J' or i == 'K' or i =='L' :
        cn += 6
    elif i == 'M' or i == 'N' or i =='O' :
        cn += 7
    elif i == 'P' or i == 'Q' or i =='R' or i =='S' :
        cn += 8
    elif i == 'T' or i == 'U' or i =='V' :
        cn += 9
    elif i == 'W' or i == 'X' or i =='Y' or i =='Z' :
        cn += 10
print(cn)