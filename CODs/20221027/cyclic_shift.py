from collections import deque

def max_bin(b):
    b = deque(b)
    max = 0
    cont = 0
    for r in range(len(b)):
        cont += 1
        b.rotate(-1)
        c = "".join(list(b))
        if int(c,2) > max : max = int(c,2)
        print(r, c,int(c,2))
    return max, cont

t = int(input())
for c in range(t):
    n,k = map(int, input().split())
    a = input()
    b = deque(list(a))
    c = "".join(list(b))
    #print(a,c,int(c,2))

    print(max_bin(c))