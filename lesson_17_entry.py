
from tkinter import *




window = Tk()
window.title("lesson 16")
window.geometry("600x500")
window.config(bg="#f4d8d8")



# ввод данных
inp_ent = Entry(width=10 , bg="#30e348" , font=("Segoe Print" , 15) , fg="#9720ff")
inp_ent.place(x= 20 , y=20)

lab_text = Label()
lab_text.place(x= 30 , y=50)

def fun_1():
    # inp_ent.get() - возвращает текст Entry
    print(type(inp_ent.get()))
    lab_text.config(text=inp_ent.get())
but_1 = Button(text="start" , command=fun_1)
but_1.place(x= 30 , y=80)



window.mainloop()