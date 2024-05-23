# 백준 25374번 등급 계산하기
# BRONZE 1
# 알고리즘 분류 : 수학, 구현, 정렬, 사칙연산
N = int(input())
li = list(map(int,input().split()))
result = [0]*9
li.sort(reverse=True)
check = [li[3],li[10],li[22],li[39],li[59],li[76],li[88],li[95],li[99]]
for i in range(N) :
    for j in range(9) :
        if li[i] < check[j] :
            continue
        else :
            result[j] += 1
            break
print(*result,sep='\n')