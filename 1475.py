#1475번 방 번호
#SILVER 5
li = list(map(int,input()))
k = [0]*10
for i in range(len(li)):
    k[li[i]] += 1
m = (k[6]+k[9])//2 + (k[6]+k[9])%2
l = 0
for i in range(10):
    if i == 6 or i == 9 :
        if l < m :
            l = m
    else :
        if l < k[i] :
            l = k[i]
print(l)