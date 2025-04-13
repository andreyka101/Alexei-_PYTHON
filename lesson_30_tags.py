from tkinter import *

window = Tk()
window.title("Касса")
window.geometry("600x500")
window.config(bg="#c4efef")


canV = Canvas(width=600 , height=500 , bg="#ffffff")
canV.place(x=0 , y=0)


canV.create_rectangle(100,100,300,300 , fill = "#8826de", tags="i_rect")


# rect1 = canV.create_rectangle(100,100,300,300 , fill = "#8826de")



canV.create_oval(0 , 0 , 70 , 70, fill = "#F4FF25", tags="i_rect i_oval")



def fun(e):
    canV.coords("i_rect" , 300 , 300 , 500 , 500)
    canV.itemconfig("i_rect" ,fill="#19FBFF" ,width=10)

    canV.itemconfig("i_oval" , outline = "#FF0808" , fill="#3C3C3C")



    # canV.coords(rect1 , 300 , 300 , 500 , 500)
    # canV.itemconfig(rect1 ,fill="#19FBFF" ,width=10)
window.bind("<KeyPress>" , fun)
window.mainloop()