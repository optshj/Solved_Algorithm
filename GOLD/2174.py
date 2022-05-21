#2174번 로봇 시뮬레이션
#GOLD 5
A,B = map(int,input().split())
N,M = map(int,input().split())
li = []
k = []
d = ["E","N","W","S"]
crashed = 0
for _ in range(N) :
    x,y,p = input().split()
    li.append([int(x),int(y),p])
for _ in range(M) :
    n,c,r = input().split()
    k.append([int(n),c,int(r)])
for _ in range(M) :
    l = k[_]
    m = li[l[0]-1]
    c = l[1]
    if c == 'L' :
        m[2] = d[(d.index(m[2])+l[2])%4]
    elif c == 'R' :
        m[2] = d[(d.index(m[2])-l[2])%4]
    else :
        for i in range(l[2]) :
            if m[2] == 'N' :
                m[1] += 1
            elif m[2] == 'E' :
                m[0] += 1
            elif m[2] == 'S' :
                m[1] -= 1
            else :
                m[0] -= 1
            for j in range(1,N+1) :
                if j == l[0] :
                    continue
                if li[j-1][0] == m[0] and li[j-1][1] == m[1] :
                    crashed = 1
                    break
            if crashed :
                print(f"Robot {l[0]} crashes into robot {j}")
                break
            if m[0] > A or m[1] > B or m[0] < 1 or m[1] < 1 :
                crashed = 1
                print(f"Robot {l[0]} crashes into the wall")
                break
    if crashed :
        break
if not crashed :
    print("OK")