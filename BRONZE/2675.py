#2675번 문자열 반복
#BRONZE 2
n = int(input())
for i in range(n):
    m = list(input())
    cnt = int(m[0])
    for i in range(2,len(m)):
        if i == len(m)-1 :
            print(m[i]*cnt)
        else :
            print(m[i]*cnt,end='')