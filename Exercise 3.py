from tkinter import*

class MyWindow:
    def __init__(self , win):
        #common widgets
        self.Label1 = Label(win , fg="Black" , bg = "aquamarine",text = "Calculator" , font = ("Helvetica Bold",24))
        self.Label1.place(x=80 , y=30)

        self.Label2 =  Label(win , text = "Number 1 : ", bg = "aquamarine" )
        self.Label2.place(x=40 , y=100)
        self.Entry1 = Entry(win , bd = 2)
        self.Entry1.place(x = 120 , y = 100)

        self.Label3 = Label(win, text="Number 2 : ", bg="aquamarine")
        self.Label3.place(x=40, y=140)
        self.Entry2 = Entry(win, bd=2)
        self.Entry2.place(x=120, y=140)

        self.Label4 = Label(win, text="Result : ", bg="aquamarine")
        self.Label4.place(x=40, y=180)
        self.Entry3 = Entry(win, bd=2)
        self.Entry3.place(x=120, y=180)

        self.Button1 = Button(win , fg = "White" , text = "Add" , command = self.add , bg = "#3A4C8B")
        self.Button1.place(x=50, y=240 )

        self.Button2 = Button(win, fg="White", text="Sub", command = self.sub , bg = "#3A4C8B")
        self.Button2.place(x=100, y=240)

        self.Button2 = Button(win, fg="White", text="Multi", command = self.multi , bg = "#3A4C8B")
        self.Button2.place(x=150, y=240)

        self.Button2 = Button(win, fg="White", text="Div", command = self.div , bg = "#3A4C8B")
        self.Button2.place(x=205, y=240)
        win.config(bg="aquamarine")



    def add(self):
        self.Entry3.delete(0 , 'end')
        num1 = float(self.Entry1.get())
        num2 = float(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def sub(self):
        self.Entry3.delete(0, 'end')
        num1 = float(self.Entry1.get())
        num2 = float(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def multi(self):
        self.Entry3.delete(0, 'end')
        num1 = float(self.Entry1.get())
        num2 = float(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def div(self):
        self.Entry3.delete(0, 'end')
        num1 = float(self.Entry1.get())
        num2 = float(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))



window = Tk()
MyWin = MyWindow(window)
window.geometry("300x350+10+10")
window.title("Standard Calculator")
window.mainloop()
