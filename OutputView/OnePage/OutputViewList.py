import tkinter
import OutputView.OnePage.OutputViewBase

class OutputViewList(OutputView.OnePage.OutputViewBase.BaseWindowShow):
    def __init__(self):
        super().__init__()
        self.mylist = tkinter.Listbox(self.win,width = 800,height = 700)
        self.mylist.pack()

    def adddata(self,data):
        self.mylist.insert(tkinter.END,data)


# b = OutputViewList()
# b.adddata('a')
# b.adddata('b')
# b.adddata('c')
# b.show()
