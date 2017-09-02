import tkinter

class BaseWindowShowPages:
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.geometry('800x700+0+0')
        self.numlist1 = tkinter.Listbox(self.win,width = 8,height = 70)
        self.numlist1.place(x = 0, y = 0)

    def show(self):
        self.win.mainloop()

    def adddata(self,data):
        pass

# b = BaseWindowShowPages()
# b.show()