from tkinter import *
from tkinter import ttk



window = Tk()
window.title("Касса")
window.geometry("900x500")
window.config(bg="#c4efef")


lab = Label(text="text" , font=("" , 14))
lab.place(x=30 , y=60)




# def fun_motion(event):
    # lab.config(text=event)
#     lab.config(text=event.state)
# window.bind("<Motion>" , fun_motion)



# def fun_button1(event):
#     lab.config(text=event)
#     # lab.config(text=event.state)
# window.bind("<Button-1>" , fun_button1)



# def fun_button2(event):
#     lab.config(text=event)
#     # lab.config(text=event.state)
# window.bind("<Button-2>" , fun_button2)



# def fun_button3(event):
#     lab.config(text=event)
#     # lab.config(text=event.state)
# window.bind("<Button-3>" , fun_button3)



# def fun_mouse_wheel(event):
#     lab.config(text=event)
#     # lab.config(text=event.state)
# window.bind("<MouseWheel>" , fun_mouse_wheel)


window.mainloop()