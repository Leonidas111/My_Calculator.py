from tkinter import*
import parser 

screen = Tk()
screen.title("My calculator")
display = Entry(screen, font=("Consol 19"))
display.grid(row=0,column=0,columnspan=6,padx=12,pady=6, sticky=W+E)
#BUTTON OPERATION:
i = 0
def add_element(element):
    global i
    display.insert(i,element)
    i = (i+1)
def clear_screen():
    display.delete(0,END)
def delete_element():
    display_status = display.get()
    if len(display_status):
        display_new_status = display_status[:-1]
        clear_screen()
        display.insert(0,display_new_status)
    else:
        clear_screen()
def calcute():
    try:
        screen_status = display.get()
        operation_math = parser.expr(screen_status).compile()
        product = eval(operation_math)
        clear_screen()
        display.insert(0,product)
    except SyntaxError:
        clear_screen()
        display.insert(0,"ERROR")

#BUTTONS COLUMN 0:
Button(screen,text="⌫",font="Consol 14",command=lambda:delete_element()).grid(row=1,rowspan=2,column=0,padx=12,pady=6,sticky=W+E+N+S)
Button(screen,text="AC",font="Consol 14",command=lambda:clear_screen()).grid(row=3,rowspan=2,column=0,padx=12,pady=6,sticky=W+E+N+S)
#BUTTONS COLUMN 1:
Button(screen,text="7",font="Consol 14",command=lambda:add_element(7)).grid(row=1,column=1,pady=6,sticky=W+E)
Button(screen,text="4",font="Consol 14",command=lambda:add_element(4)).grid(row=2,column=1,pady=6,sticky=W+E)
Button(screen,text="1",font="Consol 14",command=lambda:add_element(1)).grid(row=3,column=1,pady=6,sticky=W+E)
Button(screen,text="0",font="Consol 14",command=lambda:add_element(0)).grid(row=4,column=1,columnspan=2,pady=6,sticky=W+E)
#BUTTONS COLUMN 2:
Button(screen,text="8",font="Consol 14",command=lambda:add_element(8)).grid(row=1,column=2,sticky=W+E)
Button(screen,text="5",font="Consol 14",command=lambda:add_element(5)).grid(row=2,column=2,sticky=W+E)
Button(screen,text="2",font="Consol 14",command=lambda:add_element(2)).grid(row=3,column=2,sticky=W+E)
#BUTTONS COLUMN 3:
Button(screen,text="9",font="Consol 14",command=lambda:add_element(9)).grid(row=1,column=3,sticky=W+E)
Button(screen,text="6",font="Consol 14",command=lambda:add_element(6)).grid(row=2,column=3,sticky=W+E)
Button(screen,text="3",font="Consol 14",command=lambda:add_element(3)).grid(row=3,column=3,sticky=W+E)
Button(screen,text=".",font="Consol 14",command=lambda:add_element(".")).grid(row=4,column=3,sticky=W+E)
#BUTTONS COLUMN 4:
Button(screen,text="+",font="Consol 14",command=lambda:add_element("+")).grid(row=3,column=4,sticky=W+E)
Button(screen,text="-",font="Consol 14",command=lambda:add_element("-")).grid(row=4,column=4,sticky=W+E)
Button(screen,text="x",font="Consol 14",command=lambda:add_element("*")).grid(row=1,column=4,sticky=W+E)
Button(screen,text="÷",font="Consol 14",command=lambda:add_element("/")).grid(row=2,column=4,sticky=W+E)
#BUTTONS COLUMN 5:
Button(screen,text="expon",font="Consol 14",command=lambda:add_element("**")).grid(row=1,column=5,padx=12,sticky=W+E)
Button(screen,text="resid",font="Consol 14",command=lambda:add_element("%")).grid(row=2,column=5,padx=12,sticky=W+E)

Button(screen,text="=",font="Consol 14",command=lambda:calcute()).grid(row=3,rowspan=2,padx=12,column=5,pady=6,sticky=W+E+N+S)


screen.mainloop()