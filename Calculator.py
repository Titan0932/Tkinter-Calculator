from tkinter import * 
from types import LambdaType


root=Tk()
root.title("Simple Calculator")

output=Entry(root,width=40,borderwidth=2,font=('default',12))


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
    
    
one= Button(root, text="1", padx=3, pady=1, width=8, height=2, command=lambda: clicked(1))        # Lambda: is needed if arguments are passed on to a function
two= Button(root, text="2", padx=3, pady=1, width=8, height=2, command=lambda: clicked(2))
three= Button(root, text="3", padx=3, pady=1, width=8, height=2, command=lambda: clicked(3))
four= Button(root, text="4", padx=3, pady=1, width=8, height=2, command=lambda: clicked(4))
five= Button(root, text="5", padx=3, pady=1, width=8, height=2, command=lambda: clicked(5))
six= Button(root, text="6", padx=3,  pady=1, width=8, height=2, command=lambda: clicked(6))
seven= Button(root, text="7", padx=3, pady=1, width=8, height=2, command=lambda: clicked(7))
eight= Button(root, text="8", padx=3, pady=1, width=8, height=2, command=lambda: clicked(8))
nine= Button(root, text="9", padx=3, pady=1, width=8, height=2, command=lambda: clicked(9))
zero= Button(root, text="0", padx=3, pady=1, width=8, height=2, command=lambda: clicked(0))

multipy= Button(root, text="*", padx=3, pady=1, width=8, height=2, command=multiply)
divide= Button(root, text="/",padx=3,pady=1,width=8,height=2, command=divide)
subtract= Button(root, text="-", padx=3, pady=1, width=8, height=2, command=subtract)
add= Button(root, text="+", padx=3, pady=1, width=8, height=2, command=add)
equals= Button(root, text="=", padx=3, pady=1, width=8, height=2, command=equals, bg="grey")
clear= Button(root, text="DEL", padx=3, pady=1, width=8, height=2, command=cleared, bg="red")


def disp_calc(one,two,three,four,five,six,seven,eight,nine,zero,multipy,divide,subtract,add,equals,clear):
    
    output.grid(row=0,column=0,columnspan=4,padx=3,pady=50, ipady=10)

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