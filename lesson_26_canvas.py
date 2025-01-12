from tkinter import *

window = Tk()
window.title("Касса")
window.geometry("600x500")
window.config(bg="#c4efef")


canV = Canvas(width=600 , height=500 , bg="#ffffff")
canV.place(x=0 , y=0)


canV.create_line(10 , 10 ,100 ,200 , 60 , 500 , 500 , 100, fill = "#ba0000"  , width=10)



canV.create_rectangle(100,100,300,300 , fill = "#8826de" , outline="#f1ff27" , width=10)



canV.create_rectangle(0,0,600,500 , fill = "#ffffff" , width=0)



canV.create_polygon(10 , 10 ,100 ,200 , 60 , 500 , 500 , 100, fill = "#058a0d" , outline="#f1ff27" , width=10)






window.mainloop()