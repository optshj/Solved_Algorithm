# 백준 4659번 비밀번호 발음하기
# SILVER 5
# 메모리 : 30840KB , 시간 : 64ms, 언어 : Python3, 코드 길이 : 805B
import sys
li = ['a','e','i','o','u']
while True :
    a = sys.stdin.readline().rstrip()
    if a == "end" :
        break
    check = [0]*3
    for i in range(len(a)) :
        if a[i] in li :
            check[0] = 1
            break
    for i in range(len(a)-1) :
        if a[i] == a[i+1] :
            if a[i] == 'e' or a[i] == 'o' :
                continue
            check[1] = 1
            break
    for i in range(len(a)-2) :
        if a[i] in li and a[i+1] in li and a[i+2] in li :
            check[2] = 1
            break
        elif a[i] not in li and a[i+1] not in li and a[i+2] not in li :
            check[2] = 1
            break
    if check[0] != 1 or check[1] == 1 or check[2] == 1 :
        print(f"<{a}> is not acceptable.") 
    else :
        print(f"<{a}> is acceptable.")