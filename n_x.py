from tkinter import *

def click_button():
    global click
    click += 1
    label_clicer.configure(text=click)

click = 0
window = Tk()
window.title("Кликер")
window.geometry("980x720")

label_clicer = Label(window, text= click , font=("Arial Black", 18))
label_clicer.place(x=460 , y = 250)

button_counter = Button(window, text= "Нажимай", command=click_button, font=("Segoe Print", 25), fg="#3d04f7")
button_counter.place(x=380 , y = 300)


window.mainloop()