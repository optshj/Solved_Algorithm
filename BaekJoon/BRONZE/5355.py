#5355�� ȭ�� ����
#BRONZE 2
n = int(input())
for i in range(n):
    m = list(map(str,input().split()))
    result = float(m[0])

    for i in range(1,len(m)):
        if m[i] == '@' :
            result *= 3
        elif m[i] == '%' :
            result += 5
        elif m[i] =='#' : 
            result -= 7
    print(f'{result:.2f}')