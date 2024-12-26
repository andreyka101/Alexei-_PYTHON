from array import array
import threading
import random
import time

arr = array("i")

for i in range(10000):
    arr.append(random.randint(1,1000))




def mini_sort_1():
    global arr_1
    for el in arr_1:
        for index in range(len(arr_1)-1):
            if(arr_1[index] > arr_1[index+1]):
                element = arr_1[index]
                arr_1[index] = arr_1[index+1]
                arr_1[index + 1] = element

def mini_sort_2():
    global arr_2
    for el in arr_2:
        for index in range(len(arr_2)-1):
            if(arr_2[index] > arr_2[index+1]):
                element = arr_2[index]
                arr_2[index] = arr_2[index+1]
                arr_2[index + 1] = element





def fun_sort(arr_loc):
    global arr_1
    global arr_2
    arr_1 = array(arr_loc.typecode)
    arr_2 = array(arr_loc.typecode)
    for i in range(len(arr_loc) // 2):
        # print(arr_loc[i])
        arr_1.append(arr_loc[i])
    for i in range(len(arr_loc) // 2 , len(arr_loc)):
        # print(arr_loc[i])
        arr_2.append(arr_loc[i])


    # print(arr_1)
    # print(arr_2)
    thread_1 = threading.Thread(target = mini_sort_1)
    thread_1.start()
    thread_2 = threading.Thread(target = mini_sort_2)
    thread_2.start()
    thread_1.join()
    thread_2.join()

    # print(arr_1)
    # print(arr_2)

    
    new_arr = array(arr_loc.typecode)

    num_1 = 0
    num_2 = 0
    end_1 = False
    end_2 = False
    while(len(new_arr) != len(arr_loc)):
        if(end_2):
            new_arr.append(arr_1[num_1])
            num_1+=1
        elif(end_1):
            new_arr.append(arr_2[num_2])
            num_2+=1
        elif(arr_1[num_1] < arr_2[num_2]):
            new_arr.append(arr_1[num_1])
            num_1+=1
        elif(arr_2[num_2] < arr_1[num_1]):
            new_arr.append(arr_2[num_2])
            num_2+=1
        elif(arr_2[num_2] == arr_1[num_1]):
            new_arr.append(arr_1[num_1])
            new_arr.append(arr_2[num_2])
            num_1+=1
            num_2+=1
        if(len(arr_1) == num_1):
            # num_1 -= 1
            end_1 = True
        if(len(arr_2) == num_2):
            # num_2 -= 1
            end_2 = True
        
    return new_arr
        





# print(arr)
# print(fun_sort(arr))



old_time = time.time()
fun_sort(arr)
print(time.time() - old_time)
# 6.090689659118652