# задачи на строки (str):
# https://okpython.net/python/python_zadachnik/python_zadachnik.html#ex_2



# задачи на условия (if else):
# https://metanit.com/python/practice/2.php
# https://okpython.net/python/python_zadachnik/python_zadachnik.html#ex_9



# задачи на циклы (for, while):
# https://metanit.com/python/practice/3.php
# https://okpython.net/python/python_zadachnik/python_zadachnik.html#ex_10



# задачи на списки (array):
# https://pythonist.ru/python-spiski-zadachi-dlya-nachinayushhih/
# https://metanit.com/python/practice/4.php
# https://okpython.net/python/python_zadachnik/python_zadachnik.html#ex_3



# задачи на объекты (object):
# https://okpython.net/python/python_zadachnik/python_zadachnik.html#ex_5
# https://metanit.com/python/practice/8.php
# https://pythonist.ru/python-slovari-zadachi-dlya-nachinayushhih/



# задачи на функции (function):
# https://okpython.net/python/python_zadachnik/python_zadachnik.html#ex_12
# https://pynative.com/python-functions-exercise-with-solutions/
# https://proglib.io/p/funkcii-v-python-5-zadach-dlya-trenirovki-args-kwargs-i-lambda-funkciy-2022-06-15



# задачи на рекурсию (function):
# (внизу) https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23
# https://w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php



# задачи на классы (class):
# номер 1
# Создать класс, описывающий автомобиль (производитель, 
# модель, год выпуска, средняя скорость), и следующие функции 
# для работы с этим объектом.
# 1. Функция для вывода на экран информации об автомобиле.
# 2. Функция для подсчета необходимого времени для преодоления переданного расстояния со средней скоростью.

# номер 2
# создать класс колькулятор 
# в конструкторе нужно в писать 2 числа
# создать 4 метода: умножение , деление , сумма , вычитание
# создать метод для добавления числа (его можно вызвать много раз и подучить много чисел)

# https://okpython.net/python/python_zadachnik/python_zadachnik.html#ex_13



# задачи на лямбду (lambda):
# номер 1
# дан список чисел все числа которые равны 1, 2, 3 должны стать числом 0 

# номер 2
# дан список чисел и строк убрать все строки из списка

# номер 3
# даны два списка чисел которые имеют одинаковый размер 
# написать программу которая сравнивает элемент каждого списков и сохраняет самый большой
# пример: 
#     даны списки
#         ar1 = [1,3,6]
#         ar2 = [3,9,2]
#         ответ : [3,9,6]

# ar1 = [1,3,6 , 5]
# ar2 = [3,9,2 , 5]
# arr_answer = list(map(lambda x , y: (y if(y > x) else x) , ar1 , ar2))
# print(arr_answer)

# num = 3
# global num

# номер 4
# дан список в котором списки с числами ,каждое число списка умножить на num
# переменная num прибавляется на 1 с каждым новым списком (num изначально равен 2)


# num = 2
# arr_1 = [1,2,3,7,8]
# def fun(x):
#     global num
#     num += 1
#     return x * num
# arr_answer = list(map(fun, arr_1 ))
# print(arr_answer)

#Задачи на файлы (open)










# задачи на файлы (open):
# номер 1
# сделать программу , которая принимает текст и сохраняет в файл 
# text = input("Введите текст: ")
# test_file = open("study.txt","w" , encoding = "UTF-8")
# print(test_file)
# test_file.write(text)
# test_file.close


# номер 2
# сделать программу калькулятор с историей программа должна показывать историю


# номер 3
# создайте менеджер пользователей
# . программа должна работать до тех пор пока не не будет введено exit или ex
# . если ввести new - создаётся новый пользователь он должен хранить имя и пароль (если ввести существующие имя то программа просит его изменить)
# . если ввести del - удаляется пользователь его имя и пароль
# все пользователи должны сохраняются на txt файл





# дз x
# номер 1
# создайте много поточную сортировку пузырьком






# tk start
# задача 1
# Создайте игру clicker, при нажатии на кнопку должно число увеличиваться на один

# задача 2
# Сделать игру найди кнопку, при нажатии на кнопку она перемещается в случайное место по координатам ,но не выходит за границы окна







# entry
# Задание 1. Написать программу калькулятор два entry для чисел
# кнопки выполняют действие 

# Задание 2.
# сделать страницу регистрации и входа пользователя 
# зарегистрировано может быть много пользователей





# Задание 1. Написать имитацию кассового аппарата для магазина.
# Кассир должен выбрать товар (кнопка) и ввести его количество, 
# затем выбрать следующий товар. По завершению ввода 
# вывести на экран всю сумму покупки.
# Товаров (кнопок) должно быть не меньше
# 4-х, должна отображаться их цена. 
# Предусмотреть неправильно вводимые данные.
# Должен быть список выбранных товаров.