from tkinter import *
from random import randint 

window = Tk()
window.title("ROBOT")
window.geometry("600x500")
window.config(bg="#c4efef")

canV = Canvas(width=600 , height=500 , bg="#ffffff")
canV.place(x=0 , y=0)

robot_obj = {
    "x1":1,
    "x2":50,
    "y1":1,
    "y2":50,
}

money_obj = { 
    "x1":randint(1,500),
    "x2":randint(1,500),
    "y1":randint(1,500),
    "y2":randint(1,500),

}

canV.create_rectangle(robot_obj["x1"] , robot_obj["y1"] , robot_obj["x2"] ,robot_obj["y2"] , fill="#0a3aca" , width=0)
canV.create_oval(money_obj["x1"], money_obj["y1"], money_obj["x2"], money_obj["y2"], fill="#ffff3d")

def money_press(event):
    global money_obj
    if (money_obj["x1"] == robot_obj["x1"] or money_obj["x2"] == robot_obj["x2"] or money_obj["y1"] == robot_obj["y1"] or money_obj["y2"] == robot_obj["y2"]):
        canV.create_oval(money_obj["x1"], money_obj["y1"], money_obj["x2"], money_obj["y2"], fill="#ffff3d")
        


def robot_press(event):
    # print(event.keysym)
    global robot_obj
    if(event.keysym == "Right"):
        robot_obj["x1"] += 50
        robot_obj["x2"] += 50
    elif(event.keysym == "Left"):
        robot_obj["x1"] -= 50
        robot_obj["x2"] -= 50
    elif(event.keysym == "Up"):
        robot_obj["y1"] -= 50
        robot_obj["y2"] -= 50
    elif(event.keysym == "Down"):
        robot_obj["y1"] += 50
        robot_obj["y2"] += 50

    canV.create_rectangle(0 , 0 , 600 ,500 , fill="#ffffff" , width=0)
    canV.create_rectangle(robot_obj["x1"] , robot_obj["y1"] , robot_obj["x2"] ,robot_obj["y2"] , fill="#0a3aca" , width=0)
    
window.bind("<KeyPress>" , robot_press)

window.mainloop()