
l = [3,5,4,1,2]
def bubble_sort(my_list):
    n = len(my_list)
    c = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if(my_list[j]> my_list[j+1]):
                my_list[j],my_list[j+1] =my_list[j+1],my_list[j]
                c += 1
    return(c)

print(bubble_sort(l))