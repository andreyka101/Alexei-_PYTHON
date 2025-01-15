from tkinter import *

window = Tk()
window.title("Picture")
window.geometry("600x500")
window.config(bg="#c4efef")

main_canvas = Canvas(width=600 , height=500 , bg="#e9f1e5")
main_canvas.place(x=0 , y=0)

main_canvas.create_rectangle(350, 400, 200, 200, fill="#0b14c7", outline="#f41111")

main_canvas.create_polygon(270, 100, 430, 240, 150, 200, fill="#464122")

main_canvas.create_oval(500, 10, 580, 90, fill="#f8f402")




for i in range(1 ,20):
    main_canvas.create_line(20 * i , 500, 20 * i , 400 ,  fill="#34c70b" , width=4)



main_canvas.bind("<Motion>" , lambda event:print(event.x , event.y))

window.mainloop()