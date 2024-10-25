

# num_open = open("file_a1.txt")
# print(num_open)



# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись



# num_open_2 = open("file_a1.txt","r")
# print(num_open_2)
# num_file_text_2 = num_open_2.read()
# print(num_file_text_2)



# num_open_3 = open("C:/main_brain/фаилы/del_file_global.txt","r")
# print(num_open_3)
# num_file_text_3 = num_open_3.read()
# print(num_file_text_3)



# num_open_4 = open("./data_file/file_a2.txt","r")
## num_open_4 = open("data_file/file_a2.txt","r")
# print(num_open_4)
# num_file_text_4 = num_open_4.readlines()
# print(num_file_text_4)



# num_open_5 = open("file_a1.txt","w")
# print(num_open_5)
# num_open_5.write("wdcfff")
# num_open_5.close()

# num_open_6 = open("file_a1.txt").read()
# print(num_open_6)



# num_open_7 = open("file_a1.txt","a")
# print(num_open_7)
# num_open_7.write("_456")
# num_open_7.close()



# with open("file_a1.txt","a") as num_open_8:
#     num_open_8.write("==123")





# print("1=23=456=7886=33333".split("="))
open_read_file = open("data_file/file_a3.txt", "r").read()
with open("data_file/file_a3.txt","w") as file:
    print(open_read_file)
    open_read_file = open_read_file.split("\n")
    print(open_read_file)
    save_read_file = ""
    for i in open_read_file:
        save_read_file += i
    print(save_read_file)
    file.write(save_read_file)






