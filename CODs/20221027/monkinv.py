def m_inv(m):
    cont = 0
    l = len(m)
    for i in range(l):
        for j in range(l):
            for p in range(l):
                for q in range(l):
                    #print(i,j,p,q)
                    if((m[i][j])>m[p][q] and i<=p and j <= q):
                        cont += 1
    return cont

t = int(input())
for case in range(t):
    n = int(input())
    m = []
    for l in range(n):
        m.append([int(x) for x in input().split()])
    print(m_inv(m))
