from tkinter import*
import parser

root = Tk()
root.title("MY CALCULATOR")
#INPUT CALCULATOR:
display = Entry(root)
display.grid(row=1, columnspan=3, sticky=W+E)
#RUNING BUTTONS CALCULATOR:
i = 0
def get_numbers(number):
    global i 
    display.insert(i,number)
    i = (i + 1)
def get_operators(operators):
    global i
    longoperator = len(operators)
    display.insert(i,operators)
    i = i + longoperator
def clear_display():
    display.delete(0, END)
def undo():
    display_status = display.get()
    if len(display_status):
        display_new_status = display_status[:-1]
        clear_display()
        display.insert(0,display_new_status)
    else:
        clear_display()
def calculate():
    display_state = display.get()
    try:
        math_expresion = parser.expr(display_state).compile()
        result = eval(math_expresion)
        clear_display()
        display.insert(0,result)
    except SyntaxError:
        clear_display()
        display.insert(0,"ERROR")

#NUMBER BUTTONS:
    
Button(root,text="7",command=lambda:get_numbers(7)).grid(row=3,column=0,sticky=W+E)
Button(root,text="4",command=lambda:get_numbers(4)).grid(row=4,column=0,sticky=W+E)
Button(root,text="1",command=lambda:get_numbers(1)).grid(row=5,column=0,sticky=W+E)
Button(root,text="0",command=lambda:get_numbers(0)).grid(row=6,columnspan=3,sticky=W+E)
Button(root,text="8",command=lambda:get_numbers(8)).grid(row=3,column=1,sticky=W+E)
Button(root,text="5",command=lambda:get_numbers(5)).grid(row=4,column=1,sticky=W+E)
Button(root,text="2",command=lambda:get_numbers(2)).grid(row=5,column=1,sticky=W+E)
Button(root,text="9",command=lambda:get_numbers(9)).grid(row=3,column=2,sticky=W+E)
Button(root,text="6",command=lambda:get_numbers(6)).grid(row=4,column=2,sticky=W+E)
Button(root,text="3",command=lambda:get_numbers(3)).grid(row=5,column=2,sticky=W+E)

#OPERATION BUTTONS:
    
Button(root,text="🔄",command=lambda:undo()).grid(row=1,column=3,sticky=W+E)
Button(root,text="AC",command=lambda:clear_display()).grid(row=2,column=0,sticky=W+E)
Button(root,text="/",command=lambda:get_operators("/")).grid(row=2,column=3,sticky=W+E)
Button(root,text="x",command=lambda:get_operators("*")).grid(row=3,column=3,sticky=W+E)
Button(root,text="-",command=lambda:get_operators("-")).grid(row=4,column=3,sticky=W+E)
Button(root,text="+",command=lambda:get_operators("+")).grid(row=5,column=3,sticky=W+E)
Button(root,text="=",command=lambda:calculate()).grid(row=6,column=3,sticky=W+E)
Button(root,text="%",command=lambda:get_operators("%")).grid(row=2,column=2,sticky=W+E)
Button(root,text="exp",command=lambda:get_operators("**")).grid(row=2,column=1,sticky=W+E)


root.mainloop()

