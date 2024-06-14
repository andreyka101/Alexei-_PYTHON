# *LINK - пример 1
# obj = {
#     'uu':"pupupu",
#     '5':"five",
#     2:"two",
#     "qwe": 13,
# }
# print(obj)



# *LINK - пример 2
# obj = {
#     0: 13,
#     1:"pupupu",
#     2:"five",
#     3:"two",
# }
# print(obj[1])



# *LINK - пример 2
# obj = {
#     0: 13,
#     1:"pupupu",
#     2:"five",
#     3:"two",
# }


# методы:

# obj.clear()
# print(obj)
# очищает словарь.

# print(obj)
# obj_copy = obj.copy()
# obj.clear()
# print(obj)
# print(obj_copy)
# возвращает копию словаря.

# obj.items()
# for k, v in obj.items():
#     print(k, "=", v)
# возвращает пары (ключ, значение).

# r = obj.keys()
# print(r)
# print(type(r))
# возвращает ключи в словаре.

# obj.pop(key, default)
# r = obj.pop('5')
# print(r)
# t = obj.pop('4',"000")
# print(t)
# print(obj)
# удаляет ключ, и возвращает значение. 
# Если ключа нет, возвращает default (по умолчанию бросает исключение).

# obj.popitem()
# print(obj)
# -----
# r = obj.popitem()
# print(r)
# последний элемент удаляет и возвращает пару (ключ, значение). 
# Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.

# obj.setdefault(key, default)
# r = obj.setdefault('6')
# print(r)
# t = obj.setdefault('4',"000")
# print(t)
# print(obj)
# возвращает значение ключа, но если его нет, 
# не бросает исключение, а создает ключ с значением default (по умолчанию None).

# obj.update({"ttt":9,"poi":"uuu"})
# print(obj)
# обновляет словарь, добавляя пары (ключ, значение) из other. 
# Существующие ключи перезаписываются. 
# Возвращает None (не новый словарь!).

# obj.values()
# print(type (obj.values()))
# print(obj.values())
# возвращает значения в словаре.




str_t= input("__")
# *TODO - v1
# if(str_t == "q"):
#     print(1)
# elif(str_t == "w"):
#     print(2)
# elif(str_t == "e"):
#     print(3)
# elif(str_t == "r"):
#     print(4)
# elif(str_t == "t"):
#     print(5)
# elif(str_t == "y"):
#     print(6)

# *TODO - v2
# if_object = {
#     "q":1,
#     "w":2,
#     "e":3,
#     "r":4,
#     "t":5,
#     "y":6,
# }
# print(if_object[str_t])
