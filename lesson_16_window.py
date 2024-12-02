
from tkinter import *




window = Tk()
window.title("lesson 16")
window.geometry("600x500+300+200")
window.config(bg="#0004ff")
# window.resizable(False, False) # зафиксировать размер окна

window.minsize(400,300)   # минимальный размер окна

# window.maxsize(800,700)   # максимальный размер окна



lab_text = Label(text="qweeq")
# anchor позиционирование относительно окна
lab_text.place(relx=0.5 , rely=0.5 , anchor="center")

lab_text2 = Label(text="q565656")
lab_text2.place(relx=0.5 , rely=0.1 , anchor="n")

inp_ent = Entry()
inp_ent.place(relx=0.5 , rely=0.8 , anchor="center")


def fun_1():
    # меняем ширину высоту и координаты окна через Entry
    window.geometry(inp_ent.get())
but_1 = Button(text="start" , command=fun_1)
but_1.place(relx=0.9 , rely=0.5 , anchor="center")





window.mainloop()