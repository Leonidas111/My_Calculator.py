from tkinter import*
import parser

root = Tk()
root.title("My Calculator")
display = Entry(root)
display.grid(row=1,columnspan=5,sticky=W+E)
i=0
def add_number(number):
    global i
    display.insert(i,number)
    i = (i+1)
def add_operator(operator):
    global i
    display.insert(i,operator)
    i = (i+1)
def clear_display():
    display.delete(0,END)
def delete_element():
    display_status = display.get()
    if len(display_status):
        display_new_status = display_status[:-1]
        clear_display()
        display.insert(0,display_new_status)
    else:
        clear_display()
def calculate():
    display_status = display.get()
    try:
        math_calculator = parser.expr(display_status).compile()
        result = eval(math_calculator)
        clear_display()
        display.insert(0,result)
    except SyntaxError:
        clear_display
        display.insert(0,"ERROR")



    
#BUTTONS COLUMN 0:
Button(root,text="7",command=lambda:add_number(7)).grid(row=2,column=0,sticky=W+E)
Button(root,text="4",command=lambda:add_number(4)).grid(row=3,column=0,sticky=W+E)
Button(root,text="1",command=lambda:add_number(1)).grid(row=4,column=0,sticky=W+E)
Button(root,text="0",command=lambda:add_number(0)).grid(row=5,columnspan=3,sticky=W+E)
#BUTTONS COLUMN 1:
Button(root,text="8",command=lambda:add_number(8)).grid(row=2,column=1,sticky=W+E)
Button(root,text="5",command=lambda:add_number(5)).grid(row=3,column=1,sticky=W+E)
Button(root,text="2",command=lambda:add_number(2)).grid(row=4,column=1,sticky=W+E)
#BUTTONS COLUMN 2:
Button(root,text="9",command=lambda:add_number(9)).grid(row=2,column=2,sticky=W+E)
Button(root,text="6",command=lambda:add_number(6)).grid(row=3,column=2,sticky=W+E)
Button(root,text="3",command=lambda:add_number(3)).grid(row=4,column=2,sticky=W+E)
#BUTTONS COLUMN 3:
Button(root,text="DEL",command=lambda:delete_element()).grid(row=2,column=3,sticky=W+E)
Button(root,text="x",command=lambda:add_operator("*")).grid(row=3,column=3,sticky=W+E)
Button(root,text="+",command=lambda:add_operator("+")).grid(row=4,column=3,sticky=W+E)
Button(root,text="=",command=lambda:calculate()).grid(row=5,column=3,columnspan=2,sticky=W+E)
#BUTTONS COLUMN 4:
Button(root,text="AC",command=lambda:clear_display()).grid(row=2,column=4,sticky=W+E)
Button(root,text="/",command=lambda:add_operator("/")).grid(row=3,column=4,sticky=W+E)
Button(root,text="-",command=lambda:add_operator("-")).grid(row=4,column=4,sticky=W+E)


root.mainloop()