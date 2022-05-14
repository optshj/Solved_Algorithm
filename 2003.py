#2003번 수들의 합 2
#SILVER 3
N , M = map(int,input().split())
a = list(map(int,input().split()))
end = 0
cnt = 0
c_sum = 0
for i in range(N):
    while end < N :
        if c_sum >= M :
            break
        c_sum += a[end]
        end += 1
    if c_sum == M :
        cnt += 1
    c_sum -= a[i]
print(cnt)