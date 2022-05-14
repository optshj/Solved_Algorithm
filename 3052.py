#3052번 나머지
#BROZNE 2
result = []
for i in range(10) :
    a = int(input())
    result.append(a%42)
s1 = set(result)
print(len(s1))