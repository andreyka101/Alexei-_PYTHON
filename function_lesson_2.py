# num = 0
# def run_fun(n1):
#     print(n1)
#     if (n1 != 10):
#         return run_fun(n1 + 1)


# run_fun(num)
# n2 = num
# while (n2 != 11):
#     print(n2)
#     n2+=1




# задачи
# https://ejudge.179.ru/tasks/training/recursion.html
# номер 1
# def fun_A(n , index = 1):
#     print(index)
#     if(n!=index):
#         return fun_A(n, index+1)

# fun_A(9)


# номер 2
# def fun_summ_list(arr , index = 0 , summ = 0):
#     if(len(arr) != index):
#         return fun_summ_list(arr,index+1, summ + arr[index])
#     else:
#         return summ
    
# list_global = [2,7,4,2]
# print(fun_summ_list(list_global))

# номер 3
# def fun_object_create(arr_key, arr_value, index = 0 , value_obj = {}):
#     if(len(arr_key) != len(arr_value)):
#         print("none")
#         return {}
#     if(len(arr_key) != index):
#         value_obj.update({arr_key[index]:arr_value[index]})
#         return fun_object_create(arr_key, arr_value, index +1 , value_obj)
#     else:
#         return value_obj

# arr_tit = ["ww","rr","ok"]
# arr_val = [4,9,"n"]
# print(fun_object_create(arr_tit , arr_val))