from tkinter import *

window = Tk()
window.title("Касса")
window.geometry("600x500")
window.config(bg="#c4efef")


# создание элемента Canvas
canV = Canvas(width=600 , height=500 , bg="#ffffff")
canV.place(x=0 , y=0)
# рисуем в Canvas с помощью методов




# create_line - создать линию
# fill = цвет
# width = толщина линии
# smooth = закругление углов
canV.create_line(10 , 10 ,100 ,200 , 60 , 500 , 500 , 100, fill = "#ba0000"  , width=10 , smooth= True , stipple ="gray50")
# canV.create_line(300 , 200 ,100 ,200 , 60 , 500 , fill = "#ba0000"  , width=10 , smooth= True)



# create_rectangle - создать квадрат
# fill = цвет
# width = толщина рамки
# outline = цвет рамки
# canV.create_rectangle(100,100,300,300 , fill = "#8826de" , outline="#f1ff27" , width=10)



# очистка Canvas
canV.create_rectangle(0,0,600,500 , fill = "#1bf590" , width=0)



# create_polygon - создать многоугольник
# fill = цвет
# width = толщина рамки
# outline = цвет рамки
# canV.create_polygon(10 , 10 ,100 ,200 , 60 , 500 , 500 , 100, fill = "#058a0d" , outline="#f1ff27" , width=10)



# create_oval - создать овал или круг
# fill = цвет
# width = толщина рамки
# outline = цвет рамки
canV.create_oval(40 , 40 , 250 , 250 , fill="#e9f71f" ,width=0 , outline="#1da7e2")



# create_text - создать текст
# fill = цвет
# font = размер и шрифт
# text = текст
# justify = выравнивание текста
# canV.create_text(300 , 250 , text="hello world \n2332332" , justify="center" , fill="#5600bf" , font="Arial 15")




# create_arc - создаёт дугу
# start = начальный угол дуги в градусах;
# extent = размер дуги в градусах. Дуга всегда рисуется в направлении 
# против часовой стрелки;
# fill = цвет
# width = толщина линии дуги
# outline = цвет рамки
# canV.create_arc(40 , 40 , 250 , 250 , fill="#929292" , start = 0 , extent = 360)


# style ='arc' - рамка дуги
# canV.create_arc(40 , 40 , 250 , 250 , fill="#929292" , start = 0 , extent = 160 , width = 30 , outline="#e21d1d" , style = "arc")


# style ='pieslice' - дуга с углом (стоит по умолчанию)
# canV.create_arc(40 , 40 , 250 , 250 , fill="#929292" , start = 0 , extent = 90, outline="#e21d1d" , style = "pieslice")


# style ='chord' - дуга без угла
# canV.create_arc(40 , 40 , 250 , 250 , fill="#929292" , start = 0 , extent = 90, outline="#e21d1d" , style = "chord")





window.mainloop()