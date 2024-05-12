# max_X = int(input("--"))
# for i in range(5):
#     num_X = int(input("--"))
#     if(max_X< num_X):
#         max_X = num_X
# print(max_X)



# max_X = int(input("--"))
# for i in range(5):
#     max_X = max(num_X,max_X)
# print(max_X)





# for i in range(5,10):
#     print(i)




# num = int(input("--"))
# index = 0
# w = 0
# while(index <= num):
#     index += 1
#     if(index % 2 == 0):
#         print(index)
#         w+=1
# print("w =", w)





num = int(input("--"))
index = 1
num_if = 0
while(index < num - 1):
    index += 1
    print(index)
    print(index % num)
    if(index % num == 0):
        # print(index)
        num_if += 1
if (num_if == 0):
    print("num простое")
else:
    print("num 000")

