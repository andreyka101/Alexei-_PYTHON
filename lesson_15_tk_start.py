# импортируем библиотеку tkinter
from tkinter import *



# создаём окно
window = Tk()
# меняем название окна
window.title("lesson 15")
# меняем ширину и высоту окна 
window.geometry("600x500")



# создаём текст через Label
# bg= цвет фона 
# fg= цвет текстам
# font = шрифт и размер текста 
lab_text_1 = Label(text="qwertyu" , bg="#84ff9d" , font=("Segoe Print" , 15) , fg="#e82f57")
lab_text_1.place(x=500 , y = 20 , width= 170 , height=30)



lab_text_2 = Label(text="text_2")
lab_text_2.place(x=10 , y = 50)



def fun_1():
    print("ok")
    # с помощью метода configure или config можно изменить параметры объекта 
    lab_text_2.config(bg="#ffd084" , text="000")
    # изменяем позицию button_1
    button_1.place(x=100 , y = 200)

# создаём кнопку command вызывает функцию
button_1 = Button(text= "click" , command=fun_1)
button_1.place(x=10 , y = 10)



def fun_2():
    # print(window.geometry())
    # получаем ширину, высоту и координаты окна
    lab_text_2.configure(text= window.geometry())
button_2 = Button(text= "geometry win" , command=fun_2)
button_2.place(x=10 , y = 80)





window.mainloop()