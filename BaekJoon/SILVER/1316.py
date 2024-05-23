#1316번 그룹 단어 체커
#SILVER 5
a = int(input())
cn = a
for i in range(a) :
    b = input()

    li = [1]*(len(b))
    
    k = 0
    re = []
    m = 0
    for j in range(len(b)-1) :
        if b[j] == b[j+1] :
            li[k] += 1
            li.pop()
        else :
            k += 1
    for f in li :
        re.append(b[m])
        m += f
    for k in re :
        if re.count(k) > 1 :
            cn -= 1
            break
print(cn)
        