# 백준 4375번 1
# SILVER 3
# 알고리즘 분류 : 수학, 브루트포스 알고리즘, 정수론
while True :
    try :
        n = int(input())
        num = 1
        while True :
            if num%n == 0 :
                print(len(str(num)))
                break
            num = num*10 + 1
    except :
        break