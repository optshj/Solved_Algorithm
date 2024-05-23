#1358¹ø ÇÏÅ°
#SILVER 4
W,H,X,Y,P = map(int,input().split())
cnt = 0
for _ in range(P) :
    x,y = map(int,input().split())
    if x <= W+X and X <= x and y <= H+Y and Y <= y:
        cnt += 1
    elif ((X-x)**2+(Y+H/2-y)**2)**0.5 <= H/2 :
        cnt += 1
    elif ((X+W-x)**2+(Y+H/2-y)**2)**0.5 <= H/2 :
        cnt += 1
print(cnt)