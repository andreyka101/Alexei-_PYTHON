from tkinter import *
import time
import math

# https://easings.net/ru



window = Tk()
window.title("Касса")
window.geometry("600x500")
window.config(bg="#c4efef")

canV = Canvas(width=600 , height=500 , bg="#ffffff")
canV.place(x=0 , y=0)


obj={
    "x1":10,
    "y1":10,
    "x2":60,
    "y2":60,
}
canV.create_rectangle(obj["x1"],obj["y1"] , obj["x2"],obj["y2"],width=0 , fill="#6E00B8")



# анимация простая
# save_time = time.time()
# while(save_time + 6 != time.time()):

#     # print(time.time() - save_time)
#     move = int(time.time() - save_time)
#     print(move)

#     canV.update()

#     canV.create_rectangle(0,0 , 600,500,width=0 , fill="#FFFFFF")
#     canV.create_rectangle(obj["x1"] + move,obj["y1"] , obj["x2"] + move,obj["y2"],width=0 , fill="#6E00B8")





# анимация с разной скоростью
# save_time = time.time()
# while(save_time + 6 != time.time()):

#     # print(time.time() - save_time)
#     move = (round(time.time() - save_time , 2)*100)
#     print(move)

#     canV.update()

#     canV.create_rectangle(0,0 , 600,500,width=0 , fill="#FFFFFF")
#     canV.create_rectangle(obj["x1"] + move,obj["y1"] , obj["x2"] + move,obj["y2"],width=0 , fill="#6E00B8")





# анимация с укореняем 
save_time = time.time()
while(save_time + 6 != time.time()):

    # print(time.time() - save_time)
    move = int(time.time() - save_time)
    print(move)

    canV.update()

    move_x_super = (obj["x1"] + move) * (obj["x1"] + move)

    canV.create_rectangle(0,0 , 600,500,width=0 , fill="#FFFFFF")
    canV.create_rectangle(move_x_super,obj["y1"] , move_x_super + 50,obj["y1"]+50,width=0 , fill="#6E00B8")




window.mainloop()




