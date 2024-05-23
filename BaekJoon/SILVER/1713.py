#1713번 후보 추천하기
#SILVER 2
N = int(input())
M = int(input())
li = list(map(int,input().split()))
K = [0]*max(li)
L = [0]*max(li)
image = []
cnt = 1
for i in li :
    K[i-1] += 1
    if i in image :
        continue
    elif len(image) != N :
        image.append(i)
    else :
        m1 = []
        m2 = []
        for j in image :
            m1.append(K[j-1])
            m2.append(L[j-1])
        if m1.count(min(m1)) > 1 :
            s = max(m2)
            for j in range(len(image)) :
                if m1[j] == min(m1) and s >= m2[j] :
                    s = m2[j]
            x = image.pop(m2.index(s))
        else :
            x = image.pop(m1.index(min(m1)))
        image.append(i)
        K[x-1] = 0
    L[i-1] = cnt
    cnt += 1
print(*sorted(image))