from tkinter import *

window = Tk()
window.title("lesson 15")
window.geometry("600x500")
window.config(bg="#ffd82d")

def fun():
    window.config(bg="#2dff5a")



num_menu = Menu(tearoff=0)
num_menu.add_command(label="butt 1")
num_menu.add_command(label="butt 2")
num_menu.add_command(label="butt 3")


main_menu = Menu()
main_menu.add_command(label="butt", command=fun)


file_menu = Menu(main_menu , tearoff=0)

file_menu.add_command(label="open")

file_menu.add_separator()

num_check = IntVar(value=1)
file_menu.add_checkbutton(variable=num_check , label="i checkbutton")

num_radio = StringVar(value="b2")
file_menu.add_radiobutton(variable=num_radio , value="b1" , label="radio 1")
file_menu.add_radiobutton(variable=num_radio , value="b2" , label="radio 2")
file_menu.add_radiobutton(variable=num_radio , value="b3" , label="radio 3")

file_menu.add_cascade(label="num" , menu=num_menu)





main_menu.add_cascade(label="file" , menu=file_menu)
main_menu.add_cascade(label="num222" , menu=num_menu)


window.config(menu=main_menu)


window.mainloop()