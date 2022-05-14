#4949¹ø ±ÕÇüÀâÈù ¼¼»ó
#SILVER 4
while True :
    a = list(str(input()))
    if a == ["."]:
        break
    li = []
    val = True
    for k in a :
        if k == "(" :
            li.append("(")

        elif k == ")" :
            if len(li) == 0 or li.pop() != "(" :
                val = False
                break

        elif k == "[":
            li.append("[")

        elif k == "]" :
            if len(li) == 0 or li.pop() != "[" :
                val = False
                break
    if len(li) != 0 :
        val = False
    if val :
        print("yes")
    else :
        print("no")