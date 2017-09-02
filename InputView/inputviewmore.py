import tkinter
import tkinter.ttk
import InputView.inputviewbase

import OutputView.OnePage.OutputViewList
import OutputView.OnePage.OutputViewTable
import OutputView.OnePage.OutputViewText
import Find.MoreFind.disk.morrefilediskfind

class  InputMoreFileView(InputView.inputviewbase.InputView_Base):
    def __init__(self):
        super().__init__()


        self.mylist = tkinter.Listbox(self.win, width=80, height=50)
        self.filepathlist=[r"E:\Python\learning\5.xiangmu\0829\csdn.txt",
                      r"E:\Python\learning\5.xiangmu\0829\nasa.txt",
                      r"E:\Python\learning\5.xiangmu\0829\kaifanglite.txt",
                      r"E:\Python\learning\5.xiangmu\0829\dangdanglite.txt"]

        for  filepath  in self.filepathlist:
            self.mylist.insert(tkinter.END, filepath)
        self.mylist.place(x=0,y=100)




        self.findtype = tkinter.StringVar()  # 变量关联com下拉框
        self.comboxfindlist = tkinter.ttk.Combobox(self.win,
                                                   textvariable=self.findtype ,
                                                   width=30)
        self.comboxfindlist["value"] = ("disk","MEM","Thread","Process","GPU","Cloud")
        self.comboxfindlist.current(0)  # m默认选第一个
        self.comboxfindlist.place(x=0, y=55)  # 位置
        self.comboxfindlist.bind("<<ComboboxSelected>>", self.selectshowfindtype)
        self.realtype ="disk"
    def selectshowfindtype(self,*args):
        self.realtype=self.comboxfindlist.get()
        print(self.realtype)

    def search(self):
        print("click")
        # morefile = Find.MoreFind.disk.morrefilediskfind.MoreFileFind_Disk
        morefile = Find.MoreFind.disk.morrefilediskfind.MoreFileFind_Disk(self.filepathlist)
        morefile.find(self.entry.get()) #根据输入检索
        morefile.showmore([OutputView.OnePage.OutputViewList.OutputViewList,
                           OutputView.OnePage.OutputViewText.OutputViewText,
                           OutputView.OnePage.OutputViewList.OutputViewList,
                           OutputView.OnePage.OutputViewText.OutputViewText, ])


# morefile=InputMoreFileView()
# morefile.find("@163.com")
# #morefile.showone(Outputview.OnePage.OuputViewList.OutputViewList)
# morefile.showmore([Outputview.OnePage.OuputViewList.OutputViewList,
#                    Outputview.OnePage.OutputViewText.OutputViewText,
#                    Outputview.OnePage.OuputViewList.OutputViewList,
#                    Outputview.OnePage.OutputViewText.OutputViewText,])






