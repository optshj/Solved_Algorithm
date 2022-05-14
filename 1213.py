#1213번 팰린드롬 만들기
#SILVER 3
a = list(str(input()))
a.sort()
li1 = []
li2 = []
cnt = -1
ans = ""
for i in a:
    if i in li1 :
        li2[cnt] += 1
        continue
    li1.append(i)
    li2.append(1)
    cnt += 1
cnt = 0
for i in range(len(li2)) :
    if li2[i]%2 == 1 :
        m = li1[i]
        cnt += 1
if cnt > 1 :
    print("I'm Sorry Hansoo")
elif len(a)%2 == 1 and cnt == 1 :
    for i in range(len(li1)) :
        ans += li1[i]*(li2[i]//2)
    print(ans + m + ans[::-1])
else :
    for i in range(len(li1)) :
        ans += li1[i]*(li2[i]//2)
    print(ans + ans[::-1])

