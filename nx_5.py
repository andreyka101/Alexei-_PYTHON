from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Line")
window.geometry("900x600")
window.config(bg="#c4efef")

def moving_horizontal(value):
    line_horizontal.place(y=int(float(value)))

def moving_vertical(value):
    line_vertical.place(x=int(float(value)))

line_horizontal = Label(bg="#000")
line_horizontal.place(x=210, y=400 , width=100 , height=2)

line_vertical = Label(text="\n|\n|\n|\n|\n|\n|\n|\n|\n")
line_vertical.place(x=200, y=350)

scale_horizontal = ttk.Scale(orient=HORIZONTAL , length=200 , from_=1 , to=600 , value=5 , command=moving_horizontal)
scale_horizontal.place(x=300 , y=5)

scale_horizontal = ttk.Scale(orient=VERTICAL , length=200 , from_=1 , to=600 , value=5 , command=moving_vertical)
scale_horizontal.place(x=200 , y=1)

window.mainloop()