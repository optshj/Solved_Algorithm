#2529번 부등호
#SILVER 2
import sys
input = sys.stdin.readline
a = int(input())
b = list(map(str,input().split()))
result = []
min = "10000000000"
max = "0"
def dfs(m):
    global min
    global max
    if m == a+1:
        c = ''.join(map(str,result))
        if int(c) < int(min) :
            min = c
        elif int(c) > int(max) :
            max = c
        return
    for i in range(10):
        if i in result :
            continue
        if m == 0:
            result.append(i)
            
        else :
            if b[m-1] == '>':
                if result[m-1] > i :
                    result.append(i)
                else:
                    continue
            else :
                if result[m-1] < i :
                    result.append(i)
                else :
                    continue
        dfs(m+1)
        result.pop()
dfs(0)
print(max)
print(min)