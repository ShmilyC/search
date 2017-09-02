import OutputView.OnePage.OutputViewBase
import OutputView.OnePage.OutputViewText
import OutputView.OnePage.OutputViewList
import OutputView.OnePage.OutputViewTable
class OneSearch:
    def __init__(self,filepath,showtype,**kwargs):
        self.file = open(filepath,'rb')
        self.showwindow = showtype(**kwargs)

    def __del__(self):
        self.file.close()

    def find(self,findstr):
        pass

    def savefile(self,path):
        pass

# path='E:\Python\learning\大数据相关数据\csdn.txt'
# #bigfind=BigdataSearch(path,Outputview.OutputViewText.OutputViewText)
# #bigfind=BigdataSearch(path,Outputview.OuputViewList.OutputViewList)
# bigfind=OneSearch(path,OutputView.OnePage.OutputViewTable.OutputViewTable,
#                   tableheadlist=["user","password","email"],splitstr=" # ")
#
# bigfind.find("@163.com")