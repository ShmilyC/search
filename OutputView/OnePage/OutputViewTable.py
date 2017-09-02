import tkinter
import tkinter.ttk
import OutputView.OnePage.OutputViewBase

class OutputViewTable(OutputView.OnePage.OutputViewBase.BaseWindowShow):
    def __init__(self,tableheadlist,splitstr):
        super().__init__()
        self.table = tkinter.ttk.Treeview(self.win,height = 800)
        self.num = 0

        self.table['columns'] = tuple(tableheadlist)
        for data in tuple(tableheadlist):
            self.table.column(data,width = 100)
            self.table.heading(data,text = data)

        self.splitstr = splitstr
        self.tableheadlist = tableheadlist
        self.table.pack(fill = tkinter.BOTH)

    def adddata(self,data):
        datalist = tuple(data.split(self.splitstr))
        if len(datalist) == len(self.tableheadlist):
            self.table.insert('',self.num,text = str(self.num),values = datalist)
            self.num += 1


# csdn= OutputViewTable(["user","password","email"]," # ")
# csdn.adddata("yincheng1 # 12321321 # yincheng@qq.com")
# csdn.adddata("yincheng2 # 12321321 # yincheng@qq.com")
# csdn.adddata("yincheng3 # 12321321 # yincheng@qq.com")
# csdn.show()