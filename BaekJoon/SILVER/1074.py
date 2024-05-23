# 백준 1074번 Z
# SILVER 1
# 알고리즘 분류 : 분할 정복, 재귀
N,r,c = map(int,input().split())
ans = 0
def find(x,y,s) :
    global ans
    if x == r and y == c :
        print(ans)
        return
    if (x <= r < x + s and y <= c < y + s) :
        find(x,y,s//2)
        find(x,y+s//2,s//2)
        find(x+s//2,y,s//2)
        find(x+s//2,y+s//2,s//2)
    else :
        ans += s**2
N = 2**N
find(0,0,N)
print(ans)