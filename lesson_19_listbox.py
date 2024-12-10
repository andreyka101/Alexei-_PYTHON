from tkinter import *

window = Tk()
window.title("lesson 16")
window.geometry("600x500")
window.config(bg="#f4d8d8")



# Listbox - Отображение списка в интерфейсе 
arr = [1,2,3,4,5]
list_box = Listbox(listvariable= Variable(value=arr))
list_box.place(x= 40 , y = 30)



lab_text = Label(text="" , font=("" , 13) )
lab_text.place(x=30 , y=220)
inp_ent = Entry()
inp_ent.place(x= 30 , y=250)




def fun_1():
    # list_box.curselection() - возвращает выбранный индекс
    print(list_box.curselection())
    lab_text.config(text = list_box.curselection())
but_1 = Button(text="get index" , command=fun_1)
but_1.place(x= 180 , y=30)




def fun_2():
    # list_box.get(i) - получаем элемент с индексом i
    print(list_box.get(0))
    lab_text.config(text = list_box.get(list_box.curselection()))
but_2 = Button(text="get list" , command=fun_2)
but_2.place(x= 180 , y=60)




def fun_3():
    # list_box.insert(x , element) - вставляет новый элемент на x индекс
    list_box.insert(0 , inp_ent.get())
but_3 = Button(text="new el" , command=fun_3)
but_3.place(x= 180 , y=90)




def fun_4():
    # list_box.delete(i) - удаляет элемент по индексу i
    list_box.delete(list_box.curselection())
but_4 = Button(text="del el" , command=fun_4)
but_4.place(x= 180 , y=120)




def fun_5():
    # замена
    list_box.insert(list_box.curselection() , inp_ent.get())
    list_box.delete(list_box.curselection())
but_5 = Button(text="rename" , command=fun_5)
but_5.place(x= 180 , y=150)





window.mainloop()