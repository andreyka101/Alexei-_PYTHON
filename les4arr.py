#REVIEW - https://metanit.com/python/practice/4.php
#LINK -  Упражнение 2
# mat = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
# print(mat[0])
# print(mat[1])
# print(mat[2])


#LINK -  Упражнение 3
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
answer = ""
for y in mat:
    # print(y)
    for x in y:
        answer += str(x) + " "
    print(answer)
    answer=""


#LINK -  Упражнение 4
#FIXME - сделать
arr = [1,3,2,1,5,1]
print(arr)
arr.remove(1)
print(arr)


