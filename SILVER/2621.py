# 백준 2621번 카드게임
# SILVER 4
# 알고리즘 분류 : 구현
color = []
num = []
score = 0
for i in range(5) :
    c,n = map(str,input().split())
    color.append(c)
    num.append(int(n))
num.sort(reverse=True)
num_cnt = [0]*5
check = 1
for i in range(5) :
    num_cnt[num.index(num[i])] += 1

for i in range(4) :
    if num[i+1] + 1 != num[i] :
        check = 0

for i in range(5) :
    if color.count(color[i]) == 5 and check:
        score = 900 + max(num)
        break
    if num.count(num[i]) == 4 :
        score = 800 + num[i]
        break

    if 3 in num_cnt and 2 in num_cnt :
        score = 700 + num[num_cnt.index(3)]*10 + num[num_cnt.index(2)]
        break

    if color.count(color[i]) == 5 :
        score = 600 + max(num)
        break

    if check :
        score = 500+ max(num)
        break

    if num.count(num[i]) == 3 :
        score = 400 + num[i]
        break

    if num_cnt.count(2) == 2 :
        num_cnt[num_cnt.index(2)] += 100
        score = 300 + num[num_cnt.index(102)]*10 + num[num_cnt.index(2)]
        break

    if num.count(num[i]) == 2 :
        score = 200 + num[i]
        break

if score :
    print(score)
else :
    print(100+max(num))