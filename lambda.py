# def fun_x():
#     return 2*3
# print(fun_x)
# print(fun_x())
# print(type(fun_x()))
# print(type(fun_x))



# lamd_x = lambda: 2*2
# print(lamd_x)
# print(lamd_x())
# print(type(lamd_x))



# print((lambda:7+1)())



# num = 2
# создание лямбды
# лямбда всегда возвращает значение
# lamb_1 = lambda: num * 3
# print(lamb_1())
# тоже самое но функция
# def fun_1():
#     return num * 3


# # передача лямбде значения
# lamb_2 = lambda x : x * 3
# print(lamb_2(4))


# # значение по умолчанию в лямбде
# lamb_3 = lambda x , y = 8 : x + y
# print(lamb_3(4))


# # условие в одну строку
# print("yes" if(1 == 1) else "not")


# num_x_2 = 4
# num_if = "one" if(num_x_2 == 1) else ("two" if(num_x_2 == 2) else (lambda x : x * 3))
# print(num_if(5))



# # условие в лямбде
# lamb_4 = lambda x , y : x+y if(x > y) else 0
# print(lamb_4(6, 5))




# map(fun, arr) - использует функцию fun к каждому элементу arr
# def fun_2(x):
#     return x * 2
arr = [2,3,4,5,6,7]
# # чтобы map корректно работала её нужно вызывать в функции list
# arr_2 = list(map(fun_2, arr))
# print(arr_2)


arr_2 = [1,2,3,4,5,1]


# map - принимает до шесть списков
# fun_3(x , y) - x элемент первого списка , y элемент второго списка
# def fun_3(x , y):
#     print(y)
#     return x + y
# arr_3 = list(map(fun_3, arr , arr_2))
# print(arr_3)


# # использование лямбды в функции map
# arr_4 = list(map(lambda x : x - 5, arr))
# print(arr_4)


# # filter - он фильтрует
# arr_5 = list(filter(lambda x : x > 4, arr))
# print(arr_5)



# def fun_4(x):
#     if(x >= 4):
#         return True
    
# arr_5 = list(filter(fun_4, arr))
# print(arr_5)


# # фильтрация каждого элемента списка который находится в списке
arr_big = [
    [6,3,2,6,8,2],
    [3,6,8,0,4,2],
    [1,2,3,4,5,6],
]
# arr_big_2 = list(map(lambda x: list(filter(lambda y : y%2 == 0 , x)) , arr_big))
# print(arr_big_2)



# def fun_big_1(x):
#     print(x)
#     return x
# arr_big = list(map(fun_big_1 , arr_big))
# print(arr_big)



# def fun_min(w):
#     print(w)
#     return w
# def fun_big_2(x):
#     print(x)
#     return list(map(fun_min , x))
# arr_big = list(map(fun_big_2 , arr_big))
# print(arr_big)




arr_big = list(map(lambda x_arr : list(map(lambda r : r + 1 , x_arr)) , arr_big))
print(arr_big)



