# 백준 25373번 벼락치기
# BRONZE 2
# 알고리즘 분류 : 수학, 많은 조건 분기
N = int(input())
if N < 28 :
    for i in range(8) :
        if N <= (i*(i+1))//2 :
            print(i)
            break
else :
    i = (N + 21)
    if i%7 != 0:
        print(i//7 + 1)
    else :
        print(i//7)