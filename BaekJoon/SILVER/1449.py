# 백준 1449번 수리공 항승
# SILVER 3
# 알고리즘 분류 : 그리디 알고리즘, 정렬
N,L = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
cnt = 1
max = 0
for i in range(N) :
    if li[max] + L <= li[i] :
        cnt += 1
        max = i
print(cnt)