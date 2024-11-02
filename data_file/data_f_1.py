
# открытие файла
# num_open = open("file_a1.txt")
# print(num_open)



# режимы открытия:
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись



# по умолчанию файл открывается в режиме 'r'

# num_open_2 = open("file_a1.txt")
# print(num_open_2)
# .read() - получаем текст отрытого файла
# num_file_text_2 = num_open_2.read()
# print(num_file_text_2)



# указываем полный путь к файлу
# num_open_3 = open("C:/main_brain/фаилы/del_file_global.txt","r")
# print(num_open_3)
# num_file_text_3 = num_open_3.read()
# print(num_file_text_3)



# указываем путь к папке с файлом
# num_open_4 = open("./data_file/file_a2.txt","r")
## num_open_4 = open("data_file/file_a2.txt","r")
# print(num_open_4)
# num_file_text_4 = num_open_4.readlines()
# print(num_file_text_4)



# выходим из двух папок
# open_file_nX = open("../../del_file_global_2.txt" , "r")
# print(open_file_nX.read())



# переписываем файл
# num_open_5 = open("file_a1.txt","w")
# print(num_open_5)
# num_open_5.write("wdcfff")

# .close() - закрывает файл
# num_open_5.close()

# если не закрыть файл то чтение не сработает
# num_open_6 = open("file_a1.txt").read()
# print(num_open_6)



# изменяем файл
# num_open_7 = open("file_a1.txt","a")
# print(num_open_7)
# num_open_7.write("_456")
# num_open_7.close()



# конструкция with сама закрывает открытый файл
# with open("file_a1.txt","a") as num_open_8:
#     num_open_8.write("==123")




# split - разбивает строку
# print("1=23=456=7886=33333".split("="))

# пример:
# open_read_file = open("data_file/file_a3.txt", "r").read()
# with open("data_file/file_a3.txt","w") as file:
#     print(open_read_file)
#     open_read_file = open_read_file.split("\n")
#     print(open_read_file)
#     save_read_file = ""
#     for i in open_read_file:
#         save_read_file += i
#     print(save_read_file)
#     file.write(save_read_file)






# дз
# номер 1
# сделать программу , которая принимает текст и сохраняет в файл 


# номер 2
# сделать программу калькулятор с историей программа должна показывать историю


# номер 3
# создайте менеджер пользователей
# . программа должна работать до тех пор пока не не будет введено exit или ex
# . если ввести new - создаётся новый пользователь он должен хранить имя и пароль (если ввести существующие имя то программа просит его изменить)
# . если ввести del - удаляется пользователь его имя и пароль
# все пользователи должны сохраняются на txt файл





