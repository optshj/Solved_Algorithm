# 백준 10972번 다음 순열
# SILVER 3
# 알고리즘 분류 : 수학, 조합론
# 메모리 : 30840KB, 시간 : 76ms, 언어 : Python3, 코드 길이 : 351B
N = int(input())
li = list(map(int,input().split()))
k = 0
check = 1
for i in range(N-1,0,-1) :
    if li[i-1] < li[i] :
        k = i-1
        break
for i in range(N-1,0,-1) :
    if li[k] < li[i] :
        li[k],li[i] = li[i],li[k]
        li = li[:k+1] + sorted(li[k+1:])
        check = 0
        print(*li)
        break
if check :
    print(-1)