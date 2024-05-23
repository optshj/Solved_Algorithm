#4948번 베르트랑 공준
#SILVER 2
def verf(i) :
    v = 2

    while i > v*v :
        if i%v == 0 :
            return False
        v += 1
    return True

while True :
    a = int(input())
    if a == 0 :
        break
    li = list(range(0,2*a+1))
    li[1] = 0
    result = 0
    i = 2
    while i*i < 2*a + 1 :
        if li[i] != 0 and verf(li[i]) :
            for j in range(i*2,2*a+1,i):
                li[j] = 0
        i += 1
    for k in range(a+1,2*a+1) :
        if li[k] != 0 :
            result += 1
    print(result)