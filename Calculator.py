from tkinter import * 
from types import LambdaType


root=Tk()
root.title("Simple Calculator")
root.minsize(width=400,height=400)
root.resizable(width=False,height=False)
canvas=Canvas(width=400,height=400,background="grey")
canvas.pack(fill=BOTH, expand=True)
output=Entry(canvas,width=40,font=('default',12),borderwidth=3,relief='solid')


sign=False

action_flag=""
answer=0
answered=False

def first_calc():
    global first
    first=output.get()
    cleared()

def add():
     
    global answer,action_flag
    first_calc()
    action_flag="+"
    output.insert(END,"+")
    

def subtract():
    global answer,action_flag
    first_calc()
    action_flag="-"
    output.insert(END,"-")

def divide():
    global answer,action_flag
    first_calc()
    action_flag="/"
    output.insert(END,"/")

def multiply():
    global answer,action_flag,first
    first_calc()
    action_flag="*"
    output.insert(END,"*")

def equals():
    global answer,action_flag,first,answered
    
    try:
        expression=output.get()
        second=expression[1:]
        if action_flag=="+":
            answer=int(first)+int(second)
        elif action_flag=="-":
            answer=int(first)-int(second)
        elif action_flag=="/":
            answer=float(int(first)/int(second))
        elif action_flag=="*":
            answer=int(first)*int(second)
            
        cleared()   
        output.insert(END,"=" + str(answer))
        answered=True
    except:
        cleared()
        output.insert(0,"ERROR DETECTED.. Press DEL")

        
        
    action_flag=""
    second=""

def cleared():
    output.delete(0,END)

def clicked(button):
    global answered
    if answered==True:
        cleared()
        answered=False
    output.insert(END,button)
    
    
one= Button(canvas, text="1", padx=3, pady=1, width=8, height=2, command=lambda: clicked(1),borderwidth=4,relief='raised')        # Lambda: is needed if arguments are passed on to a function
two= Button(canvas, text="2", padx=3, pady=1, width=8, height=2, command=lambda: clicked(2),borderwidth=4,relief='raised')
three= Button(canvas, text="3", padx=3, pady=1, width=8, height=2, command=lambda: clicked(3),borderwidth=4,relief='raised')
four= Button(canvas, text="4", padx=3, pady=1, width=8, height=2, command=lambda: clicked(4),borderwidth=4,relief='raised')
five= Button(canvas, text="5", padx=3, pady=1, width=8, height=2, command=lambda: clicked(5),borderwidth=4,relief='raised')
six= Button(canvas, text="6", padx=3,  pady=1, width=8, height=2, command=lambda: clicked(6),borderwidth=4,relief='raised')
seven= Button(canvas, text="7", padx=3, pady=1, width=8, height=2, command=lambda: clicked(7),borderwidth=4,relief='raised')
eight= Button(canvas, text="8", padx=3, pady=1, width=8, height=2, command=lambda: clicked(8),borderwidth=4,relief='raised')
nine= Button(canvas, text="9", padx=3, pady=1, width=8, height=2, command=lambda: clicked(9),borderwidth=4,relief='raised')
zero= Button(canvas, text="0", padx=3, pady=1, width=8, height=2, command=lambda: clicked(0),borderwidth=4,relief='raised')

multipy= Button(canvas, text="*", padx=3, pady=1, width=8, height=2, command=multiply,borderwidth=4,relief='raised')
divide= Button(canvas, text="/",padx=3,pady=1,width=8,height=2, command=divide,borderwidth=4,relief='raised')
subtract= Button(canvas, text="-", padx=3, pady=1, width=8, height=2, command=subtract,borderwidth=4,relief='raised')
add= Button(canvas, text="+", padx=3, pady=1, width=8, height=2, command=add,borderwidth=4,relief='raised')
equals= Button(canvas, text="=", padx=3, pady=1, width=8, height=2, command=equals, bg="grey",borderwidth=4,relief='raised')
clear= Button(canvas, text="DEL", padx=3, pady=1, width=8, height=2, command=cleared, bg="red",borderwidth=4,relief='raised')


def disp_calc(one,two,three,four,five,six,seven,eight,nine,zero,multipy,divide,subtract,add,equals,clear):
    
    output.grid(row=0,column=0,columnspan=4,padx=15,pady=50, ipady=10)

    add.grid(row=2,column=3)
    divide.grid(row=3,column=3)
    multipy.grid(row=4,column=3)
    subtract.grid(row=5,column=3)

    seven.grid(row=2,column=0)
    eight.grid(row=2,column=1)
    nine.grid(row=2,column=2)


    four.grid(row=3,column=0)
    five.grid(row=3,column=1)
    six.grid(row=3,column=2)

    one.grid(row=4,column=0)
    two.grid(row=4,column=1)
    three.grid(row=4,column=2)

    zero.grid(row=5,column=0)
    equals.grid(row=5,column=1)
    clear.grid(row=5,column=2)



disp_calc(one,two,three,four,five,six,seven,eight,nine,zero,multipy,divide,subtract,add,equals,clear)
root.mainloop()

    one.grid(row=4,column=0)
    two.grid(row=4,column=1)
    three.grid(row=4,column=2)

    zero.grid(row=5,column=0)
    equals.grid(row=5,column=1)
    clear.grid(row=5,column=2)



disp_calc(one,two,three,four,five,six,seven,eight,nine,zero,multipy,divide,subtract,add,equals,clear)
root.mainloop()
