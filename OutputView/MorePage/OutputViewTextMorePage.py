import tkinter
import OutputView.OnePage.OutputViewBase

class OutputViewText(OutputView.OnePage.OutputViewBase.BaseWindowShow):
    def __init__(self):
        super().__init__()
        self.text = tkinter.Text(self.win,width = 800,height = 700)
        self.text.pack()

    def adddata(self,data):
        self.text.insert(tkinter.INSERT,data+'\r\n')

# b= OutputViewText()
# b.adddata('a')
# b.adddata('b')
# b.adddata('c')
# b.show()