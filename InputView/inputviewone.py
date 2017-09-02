import tkinter

import OutputView.OnePage.OutputViewList
import OutputView.OnePage.OutputViewTable
import OutputView.OnePage.OutputViewText
import Find.OneFind.OneThread.OneSearchDisk
import InputView.inputviewbase


class  InputMoreView(InputView.inputviewbase.InputView_Base):
    def __init__(self):
        super().__init__()

        self.filepath = tkinter.StringVar()  # 变量关联com下拉框
        self.comboxfilelist = tkinter.ttk.Combobox(self.win,
                                                   textvariable=self.filepath,
                                                   width=60)
        self.comboxfilelist ["value"] = (r"C:\Users\Tsinghua-yincheng\Desktop\tools\csdn.txt",
                                         r"C:\Users\Tsinghua-yincheng\Desktop\tools\nasa.txt")
        self.comboxfilelist .current(0)  # m默认选第一个
        self.comboxfilelist .place(x=0, y=50)  # 位置
        self.comboxfilelist .bind("<<ComboboxSelected>>", self.selectshowfile)
        self.realfilepath=self.comboxfilelist.get()

        self.showWindow= OutputView.OnePage.OutputViewText.OutputViewText


    def  getshowtype(self):
        if self.showtype=="列表":
            self.showWindow= OutputView.OnePage.OutputViewList.OutputViewList
        elif self.showtype=="文本":
            self.showWindow = OutputView.OnePage.OutputViewText.OutputViewText
        elif  self.showtype=="表格":
            self.showWindow = OutputView.OnePage.OutputViewTable.OutputViewTable
        else:
            pass

    def search(self):
        print("click  find")
        searchstr=self.entry.get() #抓取输入文本
        print("path",self.filepath)
        myfind=Find.OneFind.OneThread.OneSearchDisk.OneSearchDisk(self.realfilepath,
                                                             self.showWindow)
        myfind.find(searchstr)#查找

    def selectshowfile(self,*args):
        self.realfilepath=self.comboxfilelist.get()
        print(self.realfilepath)

    def selectshowtype(self,*arg):
        self.showtype=self.comboxshowlist.get()
        self.getshowtype()#修改默认类型


























