from tkinter import *
from tkinter import ttk



window = Tk()
window.title("Касса")
window.geometry("900x500")
window.config(bg="#c4efef")


lab = Label(text="text" , font=("" , 14))
lab.place(x=30 , y=60)



def funPress(event):
    # event - получаем информацию о обработчике (клавиша)
    lab.config(text=event)

    # event.keysym - название клавиши
    # lab.config(text=event.keysym)

    # event.state - информация о дополнительно зажатых клавиш
    # lab.config(text=event.state)

    if(event.keycode == 87):
        window.config(bg="#FFAAAA")
    if(event.keysym == "z"):
        window.config(bg="#ff3232")
    if(event.keysym == "z" and event.state == 4):
        window.config(bg="#3287ff")
    

# обработчик нажатия клавиши клавиатуры 
window.bind("<KeyPress>" , funPress)

def funRelease(event):
    # lab.config(text=event)
    # lab.config(text=event.keysym)
    if(event.keysym == "z"):
        window.config(bg="#fffc32")
    if(event.keysym == "z" and event.state == 12):
        window.config(bg="#32ff73")


# обработчик отжатия клавиши клавиатуры
window.bind("<KeyRelease>" , funRelease)


window.mainloop()