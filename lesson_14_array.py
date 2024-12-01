from array import array


# создаём массив
# array(r , s)
# r - режим массива (размер каждой ячейки в массиве , таблица в ссылке)
# s - список (можно не писать)
arr = array("b" , [1,2,3,7,5,2])
print(arr)
print(arr[0])
arr[1] = 30
print(arr)





# array.count(х) - возвращает количество вхождений х в массив.
# array.append(х) - добавление элемента в конец массива.
# array.index(х) - номер первого вхождения x в массив.
# array.insert(n, х) - включить новый пункт со значением х в массиве перед номером n. Отрицательные значения рассматриваются относительно конца массива.
# array.pop(i) - удаляет i-ый элемент из массива и возвращает его. По умолчанию удаляется последний элемент.
# array.remove(х) - удалить первое вхождение х из массива.
# array.reverse() - обратный порядок элементов в массиве.
# array.extend(arr_2) - Расширяет список, добавляя в конец все элементы списка





# возвращает режим массива (символ при создании массива)
# print(arr.typecode)



# размер в байтах каждого элемента в массиве
# print(arr.itemsize)



# кортеж (ячейка памяти, длина масива). Полезно для низкоуровневых операций.
# print(arr.buffer_info())



# .byteswap() - преобразовывает байты
# arr.byteswap()
# print(arr)



# .tolist() - преобразование массива в список
# arr_list = arr.tolist()
# print(arr)
# print(arr_list)



# .fromlist() - добавление элементов из списка
# arr.fromlist([9,8])
# print(arr)



# .tobytes() - преобразовывает к байтам
# print(arr.tobytes())



# frombytes(x) - делает массив из байт
# arr_2 = array("b")
# arr_2.frombytes(bytes("\x02\x1e\x03\x01" , encoding = "UTF-8"))
# print(arr_2)



# .tofile(f) - сохраняет массив в открытый файл (f) , файл сохраняется в байтах
# with open("text_arr.txt" , "bw") as file:
#     arr.tofile(file)



# .fromfile(f , n) - записывает (n) чисел из (f) файла в массив , числа в файле должны быть в байтах
# arr_3 = array("b")
# with open("text_arr.txt" , "br") as file:
#     arr_3.fromfile(file , 3)
#     print(arr_3)




# сортировка пузырьком
def sort_arr(arr_loc):
    arr_mini_1 = array(arr_loc.typecode)
    arr_mini_2 = array(arr_loc.typecode)
    for el in arr_loc:
        for index in range(len(arr_loc)//2 - 1):
            if(arr_loc[index] > arr_loc[index+1]):
                element = arr_loc[index]
                arr_loc[index] = arr_loc[index+1]
                arr_loc[index + 1] = element
    return(arr_loc)

print(sort_arr(arr))



