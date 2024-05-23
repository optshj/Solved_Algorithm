#1015번 수열 정렬
#SILVER 4
N = int(input())
li = list(map(int,input().split()))
k = sorted(li)
m = [0]*max(li)
for i in range(N) :
    print(k.index(li[i]) + m[li[i]-1],end = ' ')
    m[li[i]-1] += 1