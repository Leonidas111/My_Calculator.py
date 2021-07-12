from tkinter import*

screen = Tk()
screen.title("My calculator")
display = Entry(screen, font=("Consol 14"))
display.grid(row=0,column=0,columnspan=5,padx=12,pady=6, sticky=W+E)



screen.mainloop()