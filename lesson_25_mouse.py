from tkinter import *
from tkinter import ttk



window = Tk()
window.title("Касса")
window.geometry("900x500")
window.config(bg="#c4efef")


lab = Label(text="text" , font=("" , 14))
lab.place(x=30 , y=60)




# во всех обработках мыши можно смотреть координаты



# обработчик движения мыши
# def fun_motion(event):
    # lab.config(text=event)
    # event.state - информация о зажатых клавиш
#     lab.config(text=event.state)
# window.bind("<Motion>" , fun_motion)



# обработчик нажатия лкм
# def fun_button1(event):
#     lab.config(text=event)
# # event.state - информация о дополнительно зажатых клавиш
#     # lab.config(text=event.state)
# window.bind("<Button-1>" , fun_button1)



# обработчик нажатия колёсика
# def fun_button2(event):
#     lab.config(text=event)
# event.state - информация о дополнительно зажатых клавиш
#     # lab.config(text=event.state)
# window.bind("<Button-2>" , fun_button2)



# обработчик нажатия пкм
# def fun_button3(event):
#     lab.config(text=event)
# event.state - информация о дополнительно зажатых клавиш
#     # lab.config(text=event.state)
# window.bind("<Button-3>" , fun_button3)



lab_y = 60
# обработчик вращения колёсика
def fun_mouse_wheel(event):
    # lab.config(text=event)

    global lab_y
    lab_y+=event.delta / 10
    lab.place(y= lab_y)
# event.state - информация о дополнительно зажатых клавиш
    lab.config(text=event.state)
window.bind("<MouseWheel>" , fun_mouse_wheel)



#LINK - обработчик нажатия лкм
# def fun_button1(event):
#     lab.config(text=event)
# # event.state - информация о дополнительно зажатых клавиш
#     # lab.config(text=event.state)
# window.bind("<ButtonPress>" , fun_button1)


window.mainloop()