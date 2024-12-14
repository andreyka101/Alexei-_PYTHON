from tkinter import *
from tkinter import ttk
window = Tk()
window.title("radiobutton")
window.geometry("900x700")
window.config(bg="#ff3939")


def fun_1():
    # считываем переменную
    lab_text.config(text=str(num_radio.get()))
    if(num_radio.get() == "b1"):
        window.config(bg="#f0f0f0")
    if(num_radio.get() == "b2"):
        window.config(bg="#919191")
    if(num_radio.get() == "b3"):
        window.config(bg="#3b3b3b")




# num_radio общая переменная для связи трех Radiobutton
num_radio = StringVar(value="b2")


# variable - привязка Radiobutton к переменной
rad_b1 = ttk.Radiobutton(text="but 1" , variable=num_radio , value="b1" , command=fun_1)
rad_b1.place(x=30 , y=30)

rad_b2 = ttk.Radiobutton(text="but 2" , variable=num_radio , value="b2" , command=fun_1)
rad_b2.place(x=30 , y=60)

rad_b3 = ttk.Radiobutton(text="but 3" , variable=num_radio , value="b3" , command=fun_1)
rad_b3.place(x=30 , y=90)


lab_text = Label(text=num_radio.get())
lab_text.place(x=30 , y=140)




def fun_2():
    if(num_radio_color.get() == "b1"):
        lab_text.config(bg="#fff200")
    if(num_radio_color.get() == "b2"):
        lab_text.config(bg="#1dddff")
        
num_radio_color = StringVar()
rad_b4_color = ttk.Radiobutton(text="color text 1" , variable=num_radio_color , value="b1" , command=fun_2)
rad_b4_color.place(x=170 , y=30)

rad_b5_color = ttk.Radiobutton(text="color text 2" , variable=num_radio_color , value="b2" , command=fun_2)
rad_b5_color.place(x=170 , y=60)






window.mainloop()