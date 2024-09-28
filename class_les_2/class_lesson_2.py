# Номер 1
# class Cars():
#     def __init__(self,manuf,model,year,aspeed):
#         self.manuf = manuf
#         self.model = model
#         self.year = year
#         self.aspeed = aspeed
#         self.w = 4
#         print(manuf, model,year,aspeed,sep= ",")
#     def aspd(self, dist):
#         # print()
#         return self.aspeed*dist
#     def creat_numY(self):
#         self.num_y = 5

# car_red = Cars("BMW-2","X5M-2","2022 г.в-2",120)
# print(car_red.aspd(5))

# создание переменной с помощью метода creat_numY()
# car_red.creat_numY()
# print(car_red.num_y)



# этот класс используется в файле class_main.py
class Super_class_c1():
    def __init__(self):
        self.num_n1 = 2
        self.num_n2 = 20
        self.num_n3 = 8



class Animals():
    def __init__(self , speed_num):
        self.hunger = 40
        self.speed = speed_num
    def run(self):
        print(self.speed * 5)

class Dogs(Animals):
    def stick(self):
        print("stick")
    def run(self):
        print("нет")

cat = Animals(80)
cat.run()
dog = Dogs()
dog.run()
dog.stick()