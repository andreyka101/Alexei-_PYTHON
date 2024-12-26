from tkinter import*
from tkinter import ttk



window = Tk()
window.title("Касса")
window.geometry("700x500")
window.config(bg="#c4efef")


def delet_product():
    roster_listbox.delete(0, roster_listbox.curselection())

def click_butt():
    print(product_choice.get())
    


deleted_btn = Button(text= "Удалить товар", fg="#000", command=delet_product)
deleted_btn.place(x=10, y=550)

addition_btn = Button(text= "Добавить товар", fg="#000", command=click_butt)
addition_btn.place(x=550, y=330)

list_product_lbl = Label(text="Список товаров:", font =(" Arial", 12) )
list_product_lbl.place(x=550, y=150)

bread = "Хлеб"
milk = "Молоко"
chicken_eggs = "Куриные яйца"
potato = "Картофель"
carrot = "Морковь"

product_choice = StringVar(value="none")

first_product_rbtn = ttk.Radiobutton(text= "Хлеб", variable=product_choice, value="Хлеб_40")
first_product_rbtn.place(x=550, y=180)

second_product_rbtn = ttk.Radiobutton(text= "Молоко", variable=product_choice, value="Молоко")
second_product_rbtn.place(x=550, y=210)

third_product_rbtn = ttk.Radiobutton(text= "Яйца куриные", variable=product_choice, value="Яйца куриные")
third_product_rbtn.place(x=550, y=240)

fourth_product_rbtn = ttk.Radiobutton(text= "Картофель", variable=product_choice, value="Картофель")
fourth_product_rbtn.place(x=550, y=270)

fifth_product_rbtn = ttk.Radiobutton(text= "Морковь", variable=product_choice, value="Морковь")
fifth_product_rbtn.place(x=550, y=300)

purchases_lbl = Label(text="Список покупок:", font =(" Arial", 12))
purchases_lbl.place(x=200, y=150)

array_product = []
roster_listbox = Listbox(listvariable= Variable(value=array_product))
roster_listbox.place(x=200, y=180)

window.mainloop()