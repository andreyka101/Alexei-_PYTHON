from tkinter import *



window = Tk()
window.title("Касса")
window.geometry("500x500")
window.config(bg="#c4efef")





num = 0
def fun_click(event):
    print("ok")
    element = event.widget
    print(element)
    #! получаем переменную элемента например его текст
    # lab.config(text=element["text"])

    global num 

    # if(element["text"] == 1):
    #     num += 1
    # elif(element["text"] == 2):
    #     num += 2
    # elif(element["text"] == 3):
    #     num += 3
    # elif(element["text"] == 4):
    #     num += 4
    # elif(element["text"] == 5):
    #     num += 5

    num += element["text"]

    lab.config(text=num)
    

    


obj_button = {}

for i in range(1 , 6):
    obj_button[f"but_{i}"] = Button(text=i)
    obj_button[f"but_{i}"].place(x=30 , y=(50 * i)+50)
    obj_button[f"but_{i}"].bind("<Button-1>" , fun_click)



lab = Label(text="tewdwwdxt" , font=("" , 14))
lab.place(x=50 , y=30)




window.mainloop()