from tkinter import *
from tkinter import ttk



window = Tk()
window.title("Касса")
window.geometry("500x500")
window.config(bg="#c4efef")




lab_box_1 = Label(bg="#25ffdb")
lab_box_1.place(x=0 , y=0 ,width=250 , height=250 )

lab_box_2 = Label(bg="#ff2c25")
lab_box_2.place(x=250 , y=0 ,width=250 , height=250 )

lab_box_3 = Label(bg="#f0ff25")
lab_box_3.place(x=0 , y=250 ,width=250 , height=250 )

lab_box_4 = Label(bg="#b625ff")
lab_box_4.place(x=250 , y=250 ,width=250 , height=250 )





def fun_motion(event):
    element = event.widget
    element.config(bg="#3d3d3d")
    # lab.config(text=event)
    lab.config(text=element)
window.bind("<Button-1>" , fun_motion)

def fun_button3(event):
    element = event.widget
    # lab.config(text=event)
    lab.config(text=element)

    print(type(element))
    if(str(element) == ".!label" or str(element) == ".!label2" or str(element) == ".!label3" or str(element) == ".!label4"):
        element.config(bg="#f0f0f0")
window.bind("<Button-3>" , fun_button3)




lab = Label(text="text" , font=("" , 14))
lab.place(x=30 , y=60)






window.mainloop()