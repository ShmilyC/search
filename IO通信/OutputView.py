import tkinter
class BaseWindowShow():
    def __init__(self):
        self.win=tkinter.Tk()
        self.win.geometry("800x700+0+0")
    def show(self):
        self.win.mainloop()
    def adddata(self,data):
        pass

'''
b1=BaseWindowShow()
b1.show()
'''



