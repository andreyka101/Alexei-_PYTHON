import json

arr = [1,2,3]

# print(arr)
# print(type(arr))
str_json = json.dumps(arr)
print(type(str_json))



# with open("file_J.json" , "w") as file:
#     file.write(str_json)



# with open("file_J.json" , "w") as file:
#     obj = {
#         "23":7,
#         "rrrrww":"ttt",
#         "arrs": [1,2,3],
#         6:"qwerty"
#     }
#     # file.write(json.dumps(obj))
#     json.dump(obj , file)




# arr_2 = json.loads(str_json)
# print(type(arr_2))



# with open("file_J.json") as file:
    
#     obj_1 = json.load(file)
#     print(obj_1)
#     print(type(obj_1))



