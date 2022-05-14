#1541¹ø ÀÒ¾î¹ö¸° °ıÈ£
#SILVER 2
a = list(input().split('-'))
ans = 0
for i in range(len(a)) :
    k = list(map(int,a[i].split("+")))
    if i == 0 :
        ans += sum(k)
    else :
        ans -= sum(k)
print(ans)