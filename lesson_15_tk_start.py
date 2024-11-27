from tkinter import *


window = Tk()
window.title("lesson 15")
window.geometry("600x500")



lab_text_1 = Label(text="qwertyu" , bg="#84ff9d" , font=("Segoe Print" , 15) , fg="#e82f57")
lab_text_1.place(x=500 , y = 20 , width= 170 , height=30)



lab_text_2 = Label(text="text_2")
lab_text_2.place(x=10 , y = 50)



def fun_1():
    print("ok")
    lab_text_2.config(bg="#ffd084" , text="000")
    button_1.place(x=100 , y = 200)
button_1 = Button(text= "click" , command=fun_1)
button_1.place(x=10 , y = 10)



def fun_2():
    # print(window.geometry())
    lab_text_2.configure(text= window.geometry())
button_2 = Button(text= "geometry win" , command=fun_2)
button_2.place(x=10 , y = 80)





window.mainloop()