import tkinter
import OutputView #调用外部类

class OutputViewList(OutputView.BaseWindowShow ):
    def __init__(self):
        super().__init__()#父类初始化
        self.mylist=tkinter.Listbox(self.win,width=800,height=700)
        self.mylist.pack()
    def adddata(self,data):
        self.mylist.insert(tkinter.END,data)


'''

out1=OutputViewList()
out1.adddata("a1")
out1.adddata("a2")
out1.adddata("a3")
out1.show()
'''



