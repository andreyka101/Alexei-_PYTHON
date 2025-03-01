from tkinter import *

window = Tk()
window.title("Clicker")
window.geometry("600x500")
window.config(bg="#c4efef")

main_canvas = Canvas(width=600 , height=500 , bg="#8f918f")
main_canvas.place(x=0 , y=0)

def moving(event):
    #перемещение окна при зажатии ПКМ


    window.bind("<Button-3>" , moving)

main_canvas.create_rectangle(150,200,300,350 , fill = "#1bf590" , width=0)

clicker_btn = Button(text="Клик", font=("Segoe Print" , 15) , fg="#9720ff")
clicker_btn.place(x= 200, y= 250)



window.mainloop()