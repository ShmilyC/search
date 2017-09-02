import OutputView
import OuputViewList



class BigdataSearch:
    def __init__(self,filepath,showtype,**arg):#兼容多个参数
        self.file=open(filepath,"rb")
        self.showwindow=showtype(**arg)
    def __del__(self):
        self.file.close()
    def find(self,findstr):
        pass
    def savefile(self,path):
        pass



    

'''
path="C:\\Users\\Tsinghua-yincheng\\Desktop\\tools\\csdn.txt"
#bigfind=BigdataSearch(path,Outputview.OutputViewText.OutputViewText)
#bigfind=BigdataSearch(path,Outputview.OuputViewList.OutputViewList)
bigfind=BigdataSearch(path,Outputview.OutputViewTable.OutputViewTable,
                      tableheadlist=["user","password","email"],splitstr=" # ")

bigfind.find("@163.com")

'''
