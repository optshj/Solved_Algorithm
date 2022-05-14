#1065¹ø ÇÑ¼ö
#SILVER 4
def hansu(a) :
    result = 0
    for i in range(1,a+1):
        if i < 100 :
            result += 1
        else :
            i = str(i)
            if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
                result += 1
    return result
a = int(input())
print(hansu(a))