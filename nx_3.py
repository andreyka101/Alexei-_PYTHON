from tkinter import*

window = Tk()
window.title("Касса")
window.geometry("700x500")
window.config(bg="#c4efef")

def buy():
    roster_listbox.insert(0 , product_ent.get())
addition_btn = Button(text= "Добавить товар", fg="#000", command=buy)
addition_btn.place(x=330, y=345)


def delet_product():
    roster_listbox.delete(0, roster_listbox.curselection())
deleted_btn = Button(text= "Удалить товар", fg="#000", command=delet_product)
deleted_btn.place(x=335, y=385)

purchases_lbl = Label(text="Список покупок:", font =(" Arial", 12))
purchases_lbl.place(x=200, y=150)

array_product = []
roster_listbox = Listbox(listvariable= Variable(value=array_product))
roster_listbox.place(x=200, y=180)

product_ent= Entry(bg="#f7f7f7", fg="#0d0c0d", font=("Times New Roman", 9))
product_ent.place(x=200, y=345, height=27)

def cost_product():
#итоговая сумма покупок
    1.

result_lbl = Label(text="\nИтоговая сумма:\nрублей", font =(" Arial", 10))
result_lbl.place(x=50, y=345)

window.mainloop()