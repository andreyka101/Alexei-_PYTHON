from tkinter import *
from tkinter import ttk



window = Tk()
window.title("Касса")
window.geometry("700x500")
window.config(bg="#c4efef")


# value - значение Scale
def fun(value):
    lab.config(text= int(float(value)))
    # через метод get() тоже можно получить значение Scale
    print(scale_1.get())
    lab.place(x=int(float(value)))


# ползунок
# length = длина ползунока
# from_ = старт
# to = конец
# value = значение по умолчанию
scale_1 = Scale(orient=HORIZONTAL)
scale_1.place(x=30 , y=30)


# scale_2 = ttk.Scale(orient=VERTICAL)
scale_2 = ttk.Scale(orient=HORIZONTAL , length=300 , from_=1 , to=200 , value=5 , command=fun)
scale_2.place(x=30 , y=100)


lab = Label()
lab.place(x=50,y=200)



window.mainloop()