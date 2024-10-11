num = 2
lamb_1 = lambda: num * 3
print(lamb_1())

def fun_1():
    return num * 3


lamb_2 = lambda x : x * 3
print(lamb_2(4))


lamb_3 = lambda x , y = 8 : x + y
print(lamb_3(4))


print("yes" if(1 == 2) else "not")
lamb_4 = lambda x , y : "yes" if(x > y) else "not"
print(lamb_4(4, 5))




def fun_2(x):
    return x * 2
arr = [2,3,4,5,6,7]
arr_2 = list(map(fun_2, arr))
print(arr_2)


def fun_3(x , y):
    print(y)
    return x + y
arr_3 = list(map(fun_3, arr , arr_2))
print(arr_3)


arr_4 = list(map(lambda x : x - 5, arr))
print(arr_4)


arr_5 = list(filter(lambda x : x > 4, arr))
print(arr_5)


arr_big = [
    [6,3,2,6,8,2],
    [3,6,8,0,4,2],
    [1,2,3,4,5,6],
]
arr_big_2 = list(map(lambda x: list(filter(lambda y : y%2 == 0 , x)) , arr_big))
print(arr_big_2)






