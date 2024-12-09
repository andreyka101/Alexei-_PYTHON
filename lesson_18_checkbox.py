from tkinter import *

window = Tk()
window.title("lesson 16")
window.geometry("600x500")
window.config(bg="#f4d8d8")



def fun():
    lab_text.config(text = num_check.get())
    if(num_check.get()):
        window.config(bg="#ffe51e")
    else:
        window.config(bg="#1efbff")


num_check = IntVar(value=1)
checkbox = Checkbutton(text="check" , variable=num_check , command=fun)
checkbox.place(x=30 , y=30)

lab_text = Label(text="")
lab_text.place(x=30 , y=70)

# fun()


window.mainloop()