#7567¹ø ±×¸©
#BROZNE 2
a = list(str(input()))

result = 10
for i in range(len(a)-1) :
    if a[i] == '(' and a[i+1] == '(' :
        result += 5
    elif a[i] == '(' and a[i+1] == ')' :
        result += 10
    elif a[i] == ')' and a[i+1] == ')' :
        result += 5
    elif a[i] == ')' and a[i+1] == '(' :
        result += 10
print(result)