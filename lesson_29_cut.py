# st = "1234567890-=qwerty0uiop[]"

# получаем символ 
# print(st[3])

# получаем символ с другой стороны
# print(st[-3])

# получаем 5 символов начиная с индекса 10
# print(st[5:10])

# получаем 5 символов через один начиная с индекса 10
# print(st[5:20:2])

# получаем каждый второй символ
# print(st[::2])

# получаем всю строку без двух символов в конце
# print(st[0:len(st)-2])

# получаем каждый 4 символ начиная со 2 индекса
# print(st[2::4])




# .find(s) - возвращает индекс первого вхождения строки s
# print(st.find("8"))

# .count(s) - возвращает количество вхождений строки s
# print(st.count("0"))


# .split(s) - разделяет по строке s
# str_1 = "132223-53625-7hhfgf-ff"
# print(str_1.split("-"))


# .join(x) - соединяет все строки списка x
# arr = ["123" , "456" , "789"]
# print("*".join(arr))









# str_2 = "{0} hello {1} *{2}*"
# str_2 = "{0} hello {1} *{2}*.  {0} {1}"
# print(str_2.format("hi" , "Bob" , "121"))
# str_2 = str_2.format("hi" , "Bob" , "121")
# print(str_2)



# str_2 = "{} hello {} *{}*"
# str_2 = "{} hello {} *{}*.  {} {}"
# print(str_2.format("hi" , "Bob" , "121"))



# str_2 = "{abs} hello {name}"
# print(str_2.format(abs = "hi" , name = "Bob"))



str_2 = "{arr_x[0]} hello {arr_x[1]}   arr = {arr_x}"
print(str_2.format(arr_x = [66 , "www"]))



# str_2 = "{:^30} hello"
# print(str_2.format("Bob" ))

# str_2 = "{:<30} hello"
# print(str_2.format("Bob" ))

# str_2 = "{:>30} hello"
# print(str_2.format("Bob" ))



str_2 = "{:_^30} hello"
print(str_2.format("Bob" ))

str_2 = "{:_<30} hello"
print(str_2.format("Bob" ))

str_2 = "{:_>30} hello"
print(str_2.format("Bob" ))




str_3 = "123"
# print(str_3.center(11 ))
# print(str_3.ljust(11 ))
# print(str_3.rjust(11 ))


# print(str_3.center(11 , "_"))
# print(str_3.ljust(11 , "_"))
# print(str_3.rjust(11 , "_"))








