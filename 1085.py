#1085번 직사각형에서 탈출
#BRONZE 3
x,y,w,h = map(int,input().split())
print(min([w-x,h-y,x,y]))