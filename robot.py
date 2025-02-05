from tkinter import *
from random import randint 

window = Tk()
window.title("Касса")
window.geometry("600x500")
window.config(bg="#c4efef")


# создание элемента Canvas
canV = Canvas(width=600 , height=500 , bg="#ffffff")
canV.place(x=0 , y=0)

robot_obj = {
    "x1":0,
    "x2":50,
    "y1":0,
    "y2":50,
}

num_rand_x = randint(1 , 11)
num_rand_y = randint(1 , 9)

money_obj = {
    "x1":50 * num_rand_x,
    "x2":(50 * num_rand_x) + 50,
    "y1":50 * num_rand_y,
    "y2":(50 * num_rand_y) + 50,
}


canV.create_rectangle(robot_obj["x1"] , robot_obj["y1"] , robot_obj["x2"] ,robot_obj["y2"] , fill="#0a3aca" , width=0)
canV.create_oval(money_obj["x1"], money_obj["y1"], money_obj["x2"], money_obj["y2"], fill="#ffff3d")

money_text = Label(text="coin 0" ,)
money_text.place(x=30 , y=30)

num_money = 0

def fun_press(event):
    # print(event.keysym)
    global robot_obj, money_obj , num_rand_x , num_rand_y , num_money
    if(event.keysym == "Right" and robot_obj["x2"] < 600):
        robot_obj["x1"] += 50
        robot_obj["x2"] += 50
    if(event.keysym == "Left"and robot_obj["x1"] > 0):
        robot_obj["x1"] -= 50
        robot_obj["x2"] -= 50
    if(event.keysym == "Up" and robot_obj["y1"] > 0):
        robot_obj["y1"] -= 50
        robot_obj["y2"] -= 50
    if(event.keysym == "Down" and robot_obj["y2"] < 500):
        robot_obj["y1"] += 50
        robot_obj["y2"] += 50


    # print(robot_obj["x1"] , money_obj["x1"] )
    # print(robot_obj["y1"] , money_obj["y1"] )
    # print("========================" )
    
    if(robot_obj["x1"] == money_obj["x1"] and robot_obj["x2"] == money_obj["x2"] and robot_obj["y1"] == money_obj["y1"] and robot_obj["y2"] == money_obj["y2"]):
        num_rand_x = randint(1 , 11)
        num_rand_y = randint(1 , 9)
        money_obj = {
            "x1":50 * num_rand_x,
            "x2":(50 * num_rand_x) + 50,
            "y1":50 * num_rand_y,
            "y2":(50 * num_rand_y) + 50,
            }
        num_money +=1
        money_text.config(text=f"coin {num_money}")

    
    canV.create_rectangle(0 , 0 , 600 ,500 , fill="#ffffff" , width=0)
    canV.create_rectangle(robot_obj["x1"] , robot_obj["y1"] , robot_obj["x2"] ,robot_obj["y2"] , fill="#0a3aca" , width=0)
    canV.create_oval(money_obj["x1"], money_obj["y1"], money_obj["x2"], money_obj["y2"], fill="#ffff3d")
    
window.bind("<KeyPress>" , fun_press)

window.mainloop()