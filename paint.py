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
    "x1": None,
    "x2": None,
    "y1": None,
    "y2": None,
}
def fun_motion(event):
    global line_obj
    print(event.state)
    if(event.state == 264):
        if(line_obj["x1"] == None):
            line_obj["x2"] = event.x
            line_obj["y2"] = event.y
        line_obj["x1"] = line_obj["x2"]
        line_obj["y1"] = line_obj["y2"]

        line_obj["x2"] = event.x
        line_obj["y2"] = event.y

        canV.create_line(line_obj["x1"] , line_obj["y1"] , line_obj["x2"],line_obj["y2"] , width=10)

        
    if(event.state == 8):
        line_obj = {
            "x1": None,
            "x2": None,
            "y1": None,
            "y2": None,
        }
        
    if(event.state == 1032):
        canV.create_oval(event.x - 30 , event.y - 30 , event.x + 30 , event.y + 30 , fill="#ffffff" ,width=0)
window.bind("<Motion>" , fun_motion)



window.mainloop()