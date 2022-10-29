t = int(input())
for i in range(t):
    l = [int(x) for x in input().split()]
    n, k = l[0], l[1]
    a = [int(x) for x in input().split()]
    b = []
    for j in range(k%n):
        b.insert(0, a.pop())
    c = [str(x) for x in b+a]
    print(" ".join(c))