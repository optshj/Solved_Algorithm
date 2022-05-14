#2941번 크로아티아 알파벳
#SILVER 5
a = list(input())
cn = 0
for i in range(0,len(a)-1) :
    if a[i] == 'c' and a[i+1] == '=' :
        cn += 1
    elif a[i] == 'c' and a[i+1] == '-' :
        cn += 1
    elif a[i] == 'd' and a[i+1] == '-' :
        cn += 1
    elif a[i] == 'l' and a[i+1] == 'j' :
        cn += 1
    elif a[i] == 'n' and a[i+1] == 'j' :
        cn += 1
    elif a[i] == 's' and a[i+1] == '=' :
        cn += 1
    elif a[i] == 'z' and a[i+1] == '=' :
        cn += 1
    if a[i-1] == 'd' and a[i] == 'z' and a[i+1] == '=':
        cn += 1
print(len(a)-cn)