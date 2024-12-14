from tkinter import*
from tkinter import messagebox

def click():
    username = entry_login.get()
    password = entry_password.get()
    messagebox.showinfo("Авторизация пройдена!", f"User: {username} pass: {password}")
window = Tk()
window.title("Авторизация пользователя")
window.geometry("900x700")
window.config(bg="#000")


greetings = Label(text="Добро пожаловать!", font=("monospaced", 25), fg="#33bb41", bg="black")
greetings.place(x=310, y=10)

login = Label(text="Логин", font=("Helvetica", 15), fg="aquamarine", bg="black")
login.place(x=430, y = 160)

entry_login = Entry(width=11, font=(" Arial", 13), bg="black", fg="lime")
entry_login.place(x=410, y = 200)

password = Label(text="Пароль", font=("Helvetica", 15), fg="aquamarine", bg="black")
password.place(x=420, y = 230)

entry_password = Entry(width=11, font=(" Arial", 13), bg="black", fg="lime")
entry_password.place(x=410, y = 270)

but_enter = Button(text="Войти", command=click, font=("Times New Roman", 17), fg="black", bg="purple")
but_enter.place(x=420, y=320)


window.mainloop()