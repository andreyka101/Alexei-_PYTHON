class Dogs():
    def __init__(self, step_num =2):
        """__init__(step_num =2)"""
        self.eats = 10
        self.__number = 9
        self.step = step_num
        print("class dogs")
        print(self.step)
    def feed(self):
        """hi feed"""
        self.eats += 20
    def __num_print(self):
        print(self.__number)
    def number_ret(self):
        self.__num_print()
        return self.__number

# sharik = Dogs(8)
# print(sharik.eats)
# sharik.feed()
# sharik.eats=50
# print(sharik.eats)



# print(sharik.number_ret())
# sharik.num_print()
# sharik.feed()



# dog1 = Dogs()
# print(type(dog1))



# задача 2
class TriangleChecker():
    def __init__(self, num:int):
        self.num = num
    def is_triangle(self):
        if(type(self.num) == str):
            print("Нужно вводить только числа!")
        elif(self.num < 0):
            print("С отрицательными числами ничего не выйдет!")
        elif(self.num == 0):
            print("Жаль, но из этого треугольник не сделать")

sq1 = TriangleChecker(0)
sq1.is_triangle()