from array import array
import threading

arr = array("i" , [1,2,3,7,5,2 ,5,9])




def mini_sort_1():
    global arr_1
    for el in arr_1:
        for index in range(len(arr_1)//2 - 1):
            if(arr_1[index] > arr_1[index+1]):
                element = arr_1[index]
                arr_1[index] = arr_1[index+1]
                arr_1[index + 1] = element

def mini_sort_2():
    global arr_2
    for el in arr_2:
        for index in range(len(arr_2)//2 - 1):
            if(arr_2[index] > arr_2[index+1]):
                element = arr_2[index]
                arr_2[index] = arr_2[index+1]
                arr_2[index + 1] = element





def fun_sort(arr_loc):
    global arr_1
    global arr_2
    arr_1 = array(arr.typecode)
    arr_2 = array(arr.typecode)
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


    num_1 = 0
    num_2 = 0
    while(num_1 +1 == (len(arr_loc) // 2)+1):



    


print(fun_sort(arr))