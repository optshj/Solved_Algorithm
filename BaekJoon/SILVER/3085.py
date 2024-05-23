# 백준 3085번 사탕 게임
# SILVER 3
# 알고리즘 분류 : 구현,브루트포스 알고리즘
# 메모리 : 30840 KB, 시간 : 176 ms, 언어 : Python3, 코드 길이 : 1172B

N = int(input())
li = [list(input()) for _ in range(N)]
max = 0
def count(i,j,a) :
    global max 
    cnt = 1
    if a == "v" :
        for k in range(N-1) :
            if li[k][j] == li[k+1][j] :
                cnt += 1
            else :
                cnt = 1
            if cnt > max :
                max = cnt
    elif a == "h" :
        for k in range(N-1) :
            if li[i][k] == li[i][k+1] :
                cnt += 1
            else :
                cnt = 1
            if cnt > max :
                max = cnt
for i in range(0,N) :
    for j in range(0,N) :
        count(i,j,"v")
        count(i,j,"h")
for i in range(0,N) :
    for j in range(0,N) :
        if i != N-1 and li[i][j] != li[i+1][j] :
            li[i][j],li[i+1][j] = li[i+1][j],li[i][j]
            count(i,j,"v")
            count(i+1,j,"h")
            count(i,j,"h")
            li[i][j],li[i+1][j] = li[i+1][j],li[i][j]
        if j != N-1 and li[i][j] != li[i][j+1] :
            li[i][j],li[i][j+1] = li[i][j+1],li[i][j]
            count(i,j,"v")
            count(i,j+1,"v")
            count(i,j,"h")
            li[i][j],li[i][j+1] = li[i][j+1],li[i][j]
print(max)