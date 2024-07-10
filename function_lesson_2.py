num = 0
def run_fun(n1):
    print(n1)
    if (n1 != 10):
        return run_fun(n1 + 1)


run_fun(num)
n2 = num
while (n2 != 11):
    print(n2)
    n2+=1




# задачи
# https://ejudge.179.ru/tasks/training/recursion.html
# номер 1
def fun_A(n , index = 1):
    print(index)
    if(n!=index):
        return fun_A(n, index+1)

fun_A(9,4)


# номер 2
def fun_summ_list(arr , index = 0 , summ = 0):
    if(len(arr) != index):
        return fun_summ_list(arr,index+1, summ + arr[index])
    else:
        return summ
    
list_global = [2,7,4,2]
print(fun_summ_list(list_global))


# номер 3
def fun_object_create(arr_title, arr_value, index = 0 , value_fun = {}):
    if(len(arr_title) != len(arr_value)):
        print("none")
        return {}
    if(len(arr_title) != index):
        value_fun.update({arr_title[index]:arr_value[index]})
        return fun_object_create(arr_title, arr_value, index +1 , value_fun)
    else:
        return value_fun

arr_tit = ["ww","rr","ok"]
arr_val = [4,9,"n"]
print(fun_object_create(arr_tit , arr_val))