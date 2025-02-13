from tkinter import *

window = Tk()
window.title("Касса")
window.geometry("600x500")
window.config(bg="#c4efef")


canV = Canvas(width=600 , height=500 , bg="#ffffff")
canV.place(x=0 , y=0)



arr_button = [
    {
        "x1": 100,
        "y1": 50,
        "x2": 200,
        "y2": 150,
        "background":"#8725ff",
        "click": True,
        "text": "pip",
    },
    {
        "x1": 330,
        "y1": 280,
        "x2": 500,
        "y2": 420,
        "background":"#c9ff18",
        "click": True,
        "text": "hello world",
    },
]


for i_obj in arr_button:
    # print(i_obj)
    canV.create_rectangle(i_obj["x1"],i_obj["y1"] , i_obj["x2"],i_obj["y2"], fill=i_obj["background"] , width=0)
    canV.create_text((i_obj["x1"] + i_obj["x2"])/2 , (i_obj["y1"] + i_obj["y2"])/2 , text=i_obj["text"] , justify="center" , fill="#000000" , font="Arial 15")


def fun_motion(event):
    window.title(f'{event.x} / {event.y}')
    for i_obj in arr_button:
        if((i_obj["x1"] < event.x and i_obj["x2"] > event.x) and (i_obj["y1"] < event.y and i_obj["y2"] > event.y) and i_obj["click"]):
            canV.create_rectangle(i_obj["x1"],i_obj["y1"] , i_obj["x2"],i_obj["y2"], fill="#4e4e4e" , width=0)
            canV.create_text((i_obj["x1"] + i_obj["x2"])/2 , (i_obj["y1"] + i_obj["y2"])/2 , text=i_obj["text"] , justify="center" , fill="#000000" , font="Arial 15")
        else:
            if(i_obj["click"]):
                canV.create_rectangle(i_obj["x1"],i_obj["y1"] , i_obj["x2"],i_obj["y2"], fill=i_obj["background"] , width=0)
                canV.create_text((i_obj["x1"] + i_obj["x2"])/2 , (i_obj["y1"] + i_obj["y2"])/2 , text=i_obj["text"] , justify="center" , fill="#000000" , font="Arial 15")
            else:
                canV.create_rectangle(i_obj["x1"],i_obj["y1"] , i_obj["x2"],i_obj["y2"], fill="#ff2424" , width=0)
                canV.create_text((i_obj["x1"] + i_obj["x2"])/2 , (i_obj["y1"] + i_obj["y2"])/2 , text=i_obj["text"] , justify="center" , fill="#000000" , font="Arial 15")


window.bind("<Motion>" , fun_motion)


def fun_button1(event):
    for i_obj in arr_button:
        if((i_obj["x1"] < event.x and i_obj["x2"] > event.x) and (i_obj["y1"] < event.y and i_obj["y2"] > event.y)):
            canV.create_rectangle(i_obj["x1"],i_obj["y1"] , i_obj["x2"],i_obj["y2"], fill="#ff2424" , width=0)
            canV.create_text((i_obj["x1"] + i_obj["x2"])/2 , (i_obj["y1"] + i_obj["y2"])/2 , text=i_obj["text"] , justify="center" , fill="#000000" , font="Arial 15")
            i_obj["click"] = False

        if((i_obj["x1"] > event.x or i_obj["x2"] < event.x) or (i_obj["y1"] > event.y or i_obj["y2"] < event.y)):
            canV.create_rectangle(i_obj["x1"],i_obj["y1"] , i_obj["x2"],i_obj["y2"], fill=i_obj["background"] , width=0)
            canV.create_text((i_obj["x1"] + i_obj["x2"])/2 , (i_obj["y1"] + i_obj["y2"])/2 , text=i_obj["text"] , justify="center" , fill="#000000" , font="Arial 15")
            i_obj["click"] = True
        

window.bind("<Button-1>" , fun_button1)


window.mainloop()