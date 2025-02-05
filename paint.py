from tkinter import *

window = Tk()
window.title("Касса")
window.geometry("600x500")
window.config(bg="#c4efef")


canV = Canvas(width=600 , height=500 , bg="#ffffff")
canV.place(x=0 , y=0)





# def fun_motion(event):
#     # lab.config(text=event)
#     print(event.state)
#     if(event.state == 264):
#         canV.create_oval(event.x - 15 , event.y - 15 , event.x + 15 , event.y + 15 , fill="#ffe02f" ,width=0)
#     if(event.state == 1032):
#         canV.create_oval(event.x - 30 , event.y - 30 , event.x + 30 , event.y + 30 , fill="#ffffff" ,width=0)
# window.bind("<Motion>" , fun_motion)






line_obj = {
    "x1":0,
    "x2":2,
    "y1":0,
    "y2":2,
}
def fun_motion(event):
    global line_obj

    if(event.state == 264):
        if(line_obj["x1"] == None):
            line_obj["x1"] == event.x
            line_obj["x2"] == event.x
            line_obj["y1"] == event.y
            line_obj["y2"] == event.y
        else:
            line_obj["x1"] = line_obj["x2"]
            line_obj["y1"] = line_obj["y2"]

            line_obj["x2"] = event.x
            line_obj["y2"] = event.y
            
            canV.create_line(line_obj["x1"] , line_obj["y1"] , line_obj["x2"],line_obj["y2"])
        
    if(event.state == 1032):
        canV.create_oval(event.x - 30 , event.y - 30 , event.x + 30 , event.y + 30 , fill="#ffffff" ,width=0)
window.bind("<Motion>" , fun_motion)



window.mainloop()