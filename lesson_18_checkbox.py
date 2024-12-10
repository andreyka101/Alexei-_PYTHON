from tkinter import *

window = Tk()
window.title("lesson 16")
window.geometry("600x500")
window.config(bg="#f4d8d8")



def fun():
    # получаем положение Checkbutton
    lab_text.config(text = num_check.get())
    if(num_check.get()):
        window.config(bg="#ffe51e")
    else:
        window.config(bg="#1efbff")


# в num_check хранится положения Checkbutton
num_check = IntVar(value=1)
# Checkbutton это кнопка с двумя положениями
checkbox = Checkbutton(text="check" , variable=num_check , command=fun)
checkbox.place(x=30 , y=30)

lab_text = Label(text="")
lab_text.place(x=30 , y=70)

# fun()


window.mainloop()