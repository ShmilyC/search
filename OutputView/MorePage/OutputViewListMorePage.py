import tkinter
import OutputView.MorePage.OutputViewBaseMorePage
class OutputViewListPages(OutputView.MorePage.OutputViewBaseMorePage.BaseWindowShowPages):
    def __init__(self,alllist):
        super().__init__()
        self.datalist = tkinter.Listbox(self.win,width = 120,height = 70)
        self.datalist.place(x = 30, y = 0)

        self.alllist = alllist

        for i in range(len(self.alllist)):
            self.numlist1.insert(tkinter.END,str(i))

        for data in alllist[0]:
            self.datalist.insert(tkinter.END,data)

        self.numlist1.bind('<Double-Button-1>',self.go)

    def go(self,*args):
        mytuple = self.numlist1.curselection()
        myid = mytuple[0]
        print(mytuple,myid)
        self.datalist.delete(0,tkinter.END)
        for data in self.alllist[myid]:
            self.datalist.insert(tkinter.END,data)


# alllist = [["a", "b", "c"], ["x", "y", "z"], ["m", "n", "p"]]
# my = OutputViewListPages(alllist)
# my.show()

