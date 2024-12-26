from array import array
import random
import time

arr = array("i")

for i in range(10000):
    arr.append(random.randint(1,1000))



def fun_sort(arr_loc):
    for el in arr_loc:
        for index in range(len(arr_loc)-1):
            if(arr_loc[index] > arr_loc[index+1]):
                element = arr_loc[index]
                arr_loc[index] = arr_loc[index+1]
                arr_loc[index + 1] = element
    return(arr_loc)



old_time = time.time()
fun_sort(arr)
print(time.time() - old_time)
# 12.400815963745117