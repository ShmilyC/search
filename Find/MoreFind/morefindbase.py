import OutputView.OnePage.OutputViewText
import OutputView.OnePage.OutputViewTable
import OutputView.OnePage.OutputViewList

class MoreFileFind_Base:
    def __init__(self,filepathlist):
        self.filelist=[]#文件对象列表
        for  filepath in filepathlist: #打开多个文件，文件对象加入列表，
            file=open(filepath,"rb")
            self.filelist.append(file)
            print(filepath)
        self.lastlist=[] #保存结果
        #self.lastlist=[["a","b","c"],["x","y","z"],["m","n","l"]] #测试数据
    def __del__(self):
        for file in self.filelist: #批量关闭文件
            file.close()
    def find(self,findstr):
        pass

    def showone(self,showtype):
        self.win=showtype() #text,list,table
        for  mylist  in  self.lastlist:
            for line in mylist:
                self.win.adddata(line)
        self.win.show()

    def showmore(self,showlist):
        #print(len(showlist),len(self.lastlist))
        if len(showlist)==len( self.lastlist):
            self.winlist=[]
            for  i  in  range(len(showlist)):
                mywin=showlist[i]() #动态创建一个窗体  showlist[i]是一个类型
                for  line  in  self.lastlist[i]:
                    mywin.adddata(line)
                self.winlist.append(mywin) #添加到列表
            for  mywin in self.winlist:
                mywin.show()




    def writeonefile(self,path): #写入一个文件
        save_file = open(path, "wb")
        for  mylist in self.lastlist:
            for line  in mylist:
                save_file.write(str(line).encode("utf-8"))
        save_file.close()
    def writemorefile(self,pathlist):
        for  i  in range(len(pathlist)):
            file=open(pathlist[i],"wb")
            for  line  in  self.lastlist[i]:
                file.write(str(line).encode("utf-8"))
            file.close()