#2884번 알람 시계
#BRONZE 3
h , s = map(int,input().split())
if s-45 <= 0 :
    h = h - 1
    s = s + 15
else :
    s = s - 45


if h - 1 < 0 :
    h = h + 24
    
if s == 60 :
    s = 0
    h = h + 1

if h == 24 :
    h = 0

print(f'{h} {s}')