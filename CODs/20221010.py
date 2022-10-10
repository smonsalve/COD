iteraciones = int(input("ingrese la cantidad de iteraciones a realizar: "))
#iteraciones = 15

# TODO: agregar validaciones

pi = 3

def piteration(n):
    sign = -1 if (n%2==0) else 1
    return(((4)/ ((2*n)*((2*n)+1)*((2*n)+2))))*sign



for i in range(1,iteraciones+1):
    pi += piteration(i)
    print(f"{i} -> {pi}")