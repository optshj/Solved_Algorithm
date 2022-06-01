# 백준 20365번 
# SILVER 2
# 알고리즘 분류 : 문자열, 그리디 알고리즘
def divide(a) :
    cnt = 0
    before = li[0]
    if before == a :
        cnt += 1
    for i in range(1,N) :
        if before == li[i] :
            continue
        elif before != li[i] and li[i] == a:
            before = li[i]
            cnt += 1
        else :
            before = li[i]
    return cnt

N = int(input())
li = list(input())
print(min(divide("R"),divide("B"))+1)