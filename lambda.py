num = 2
# создание лямбды
# лямбда всегда возвращает значение
lamb_1 = lambda: num * 3
print(lamb_1())
# тоже самое но функция
def fun_1():
    return num * 3


# передача лямбде значения
lamb_2 = lambda x : x * 3
print(lamb_2(4))


# значение по умолчанию в лямбде
lamb_3 = lambda x , y = 8 : x + y
print(lamb_3(4))


# условие в одну строку
print("yes" if(1 == 2) else "not")
# условие в лямбде
lamb_4 = lambda x , y : "yes" if(x > y) else "not"
print(lamb_4(4, 5))




# map(fun, arr) - использует функцию fun к каждому элементу arr
def fun_2(x):
    return x * 2
arr = [2,3,4,5,6,7]
# чтобы map корректно работала её нужно вызывать в функции list
arr_2 = list(map(fun_2, arr))
print(arr_2)


# map - принимает до шесть списков
# fun_3(x , y) - x элемент первого списка , y элемент второго списка
def fun_3(x , y):
    print(y)
    return x + y
arr_3 = list(map(fun_3, arr , arr_2))
print(arr_3)


# использование лямбды в функции map
arr_4 = list(map(lambda x : x - 5, arr))
print(arr_4)


# filter - он фильтрует
arr_5 = list(filter(lambda x : x > 4, arr))
print(arr_5)


# фильтрация каждого элемента списка который находится в списке
arr_big = [
    [6,3,2,6,8,2],
    [3,6,8,0,4,2],
    [1,2,3,4,5,6],
]
arr_big_2 = list(map(lambda x: list(filter(lambda y : y%2 == 0 , x)) , arr_big))
print(arr_big_2)






