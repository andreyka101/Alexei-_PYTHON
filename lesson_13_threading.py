import threading
import time



# пример без потока
def fun_1():
    time.sleep(5)
    print("end")

# fun_1()
# for i in range(10):
#     print(i)





# пример с потоком
# threading.Thread - создание потока
thread_1 = threading.Thread(target = fun_1)
# .start() - запуск потока 
thread_1.start()
for i in range(10):
    print(i)




# создание и запуск второго потока
def fun_2():
    time.sleep(2)
    print("fun_2 end")
thread_2 = threading.Thread(target = fun_2)

thread_2.start()





# .join() - строки ниже ждут окончание потока
thread_1.join()
print("hello")



