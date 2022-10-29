N = int(input())
data = [str(x)[-1] for x in input().split()]
print("Yes" if int("".join(data))%10 == 0 else "No")