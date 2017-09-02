import tkinter
import tkinter.ttk

class InputView_Base(object):
    def __init__(self):
        self.win=tkinter.Tk()
        self.win.geometry("600x300+0+0")
        self.win.title("BigdataFind")
        self.entry=tkinter.Entry(self.win) #输入
        self.entry.place(x=0,y=0)
        self.button=tkinter.Button(self.win,text="搜索",command=self.search)
        self.button.place(x=150,y=0)

        self.showtype=tkinter.StringVar()#变量关联com下拉框
        self.comboxshowlist=tkinter.ttk.Combobox(self.win,
                                                 textvariable=self.showtype,
                                                 width=10)
        self.comboxshowlist["value"]=("文本","列表","表格")
        self.comboxshowlist.current(0) #m默认选第一个
        self.comboxshowlist.place(x=0,y=30) #位置
        self.comboxshowlist.bind("<<ComboboxSelected>>",self.selectshowtype)
        self.showittype="文本"

    def show(self):
        self.win.mainloop()

    def search(self):
        print("click")

    def selectshowtype(self,*arg):
        self.showittype=self.comboxshowlist.get()
        print(self.showittype)



# my=InputView_Base()
# my.show()

