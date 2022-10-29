from itertools import product

def unlucky13(n):
    nums = list("0123456789")
    lista = ([str("".join(x)) for x in product(nums,repeat=n)])
    un13 = [x for x in lista if "13" not in x]
    return un13

t = int(input())
for c in range(t):
    n = int(input())
    print(len(unlucky13(n))%1000000009)
    # for i in (unlucky13(3)):
    #     print(i)


