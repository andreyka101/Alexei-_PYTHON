import threading
import time



def fun_1():
    time.sleep(5)
    print("end")


# fun_1()
# for i in range(10):
#     print(i)





thread_1 = threading.Thread(target = fun_1)

thread_1.start()
for i in range(10):
    print(i)


def fun_2():
    time.sleep(2)
    print("fun_2 end")
thread_2 = threading.Thread(target = fun_2)

thread_2.start()



thread_1.join()
print("hello")




