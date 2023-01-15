#simple calculator withought exception handling
#code lines can be reduced by using classes and for loops.

from tkinter import *

def click(event):
    global stvalue
    text=event.widget.cget("text")
    print(text)
    if(text=="hii"):
        pass
    if(text=="="):
        if(stvalue.get().isdigit()):
            value=int(stvalue.get())
        else:
            value=eval(wd.get())
        stvalue.set(value)
        wd.update()
    elif text=="c":
        stvalue.set("")
        wd.update()
    else:
        stvalue.set(stvalue.get()+text)
        wd.update()
    


root=Tk()
root.geometry("275x450")
root.title("pvm calculator")

stvalue=StringVar()
stvalue.set("")
wd=Entry(root,textvar=stvalue,font="lucida 25 bold")
wd.pack(fill=X, ipadx=10,pady=10,padx=10)

f=Frame(root, bg="skyblue")
b=Button(f,text="c",padx=5,pady=2 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="%",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="00",padx=5,pady=3 ,font="lucida 25 ")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="",padx=5,pady=3 ,font="lucida 25 ")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)


f.pack()






f=Frame(root, bg="skyblue")
b=Button(f,text="9",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="8",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="7",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="x",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root, bg="skyblue")
b=Button(f,text="4",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="5",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="6",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="-",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root, bg="skyblue")
b=Button(f,text="1",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="2",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="3",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="+",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root, bg="skyblue")
b=Button(f,text="0",padx=8,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text=".",padx=7,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="/",padx=6,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="=",padx=5,pady=3 ,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()



root.mainloop()

