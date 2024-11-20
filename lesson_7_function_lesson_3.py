# def func(n, number = 1):
#     print(number)
#     if(n > number):
#         n_copy = n
#         return func(n_copy, number + 1)
#     else:
#         return "привет"

# print(func(7))





# def func2(a, n, hash_n = 1):
#     print(a, n, hash_n)
#     print("copy")
#     if(n != 0):
#         hash_n_copy = hash_n * a
#         n_copy = n
#         a_copy = a
#         print(a_copy, n_copy, hash_n_copy)
#         print("+-+-+-+-+-+-+-+")
#         return func2(a_copy, n_copy - 1, hash_n_copy)
#     else:
#         # print("+-+-+-+-+-+-+-+")
#         return hash_n

# print(func2(5,3))




def func3(a, n = 1):
    if(n < len(str(a))):
        n_copy = n
        a_copy =  a // 10
        # print(a)
        print(a %(n * 10))
        return func3(a_copy, n_copy)
    else:
        # print(a)
        print(a)
func3(123)