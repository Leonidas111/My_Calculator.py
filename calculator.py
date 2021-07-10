from tkinter import*


root = Tk()
root.title("CALCULATOR")
#INPUT CALCULATOR:
display = Entry(root)
display.grid(row=1, columnspan=3, sticky=W+E)
i = 0
def get_numbers(number):
    global i 
    display.insert(i,number)
    i = i + 1
    
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
    
Button(root,text="🔄").grid(row=1,column=3,sticky=W+E)
Button(root,text="C").grid(row=2,column=0,sticky=W+E)
Button(root,text="/").grid(row=2,column=3,sticky=W+E)
Button(root,text="x").grid(row=3,column=3,sticky=W+E)
Button(root,text="-").grid(row=4,column=3,sticky=W+E)
Button(root,text="+").grid(row=5,column=3,sticky=W+E)
Button(root,text="=").grid(row=6,column=3,sticky=W+E)
Button(root,text="%").grid(row=2,column=2,sticky=W+E)
Button(root,text="( )").grid(row=2,column=1,sticky=W+E)


root.mainloop()

