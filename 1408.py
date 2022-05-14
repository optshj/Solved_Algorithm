#1408¹ø 24
#BRONZE 2
h1 , m1 , s1 = map(int,input().split(':'))
h2 , m2 , s2 = map(int,input().split(':'))
if s2 - s1 < 0 :
    s2 += 60
    m2 -= 1
s = s2 - s1
if m2 - m1 < 0 :
    m2 += 60
    h2 -= 1
m = m2 - m1
if h1 > h2 :
    h = h2 + 24 - h1
else :
    h = h2 - h1
if s < 10 :
    s = '0' + str(s)
if m < 10 :
    m = '0' + str(m)
if h < 10 :
    h = '0' + str(h)
print(f'{h}:{m}:{s}')