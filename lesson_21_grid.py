from tkinter import *

window = Tk()
window.title("lesson 15")
window.geometry("600x500")



#ANCHOR - все параметры grid
# column - номер ячейки по горизонтали
# row - номер ячейки по вертикали
# padx , pady - внешний оступ каждой ячейки
# ipadx , ipady - внутреннее заполнение каждой ячейки
# sticky - позиционирование элемента в ячейке
# rowspan - количество занимаемых ячеек по вертикали
# columnspan - количество занимаемых ячеек по горизонтали

lab_text_1 = Label(text="text_1" , bg="#eaba1f")
# lab_text_1.grid(column=0 , row=0 , padx=10 , pady=20)
lab_text_1.grid(rowspan=2 , column=0 , row=0 , ipadx=10 , ipady=20 , padx=10 , pady=20)

lab_text_2 = Label(text="text_2" , bg="#c9c9c9")
lab_text_2.grid(column=1 , row=0 , ipadx=100 , ipady=20)

lab_text_3 = Label(text="text_3" , bg="#ea1f1f")
lab_text_3.grid(column=1 , row=1 , ipadx=1 , ipady=2 ,sticky="sw")

lab_text_4 = Label(text="text_3" , bg="#631fea")
lab_text_4.grid(column=0 , row=1 , ipadx=1 , ipady=60 ,)




window.mainloop()