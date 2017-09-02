import OutputView
import OuputViewList
import DataFindBase
import time

class BigdataSearchDisk(DataFindBase.BigdataSearch):
    def __init__(self,filepath,showtype,**arg):#兼容多个参数
        super().__init__(filepath,showtype,**arg)

    def find(self,findstr):
        self.savelist=[] #列表用于保存结果
        while True:
            line = self.file.readline()
            line = line.decode("gbk", "ignore")
            if not line:
                break
            if line.find(findstr) != -1:#find
                print(line)
                self.savelist.append(line) #结果添加到列表
                time.sleep(1)
                self.showwindow.adddata(line)  # 多态
        self.showwindow.show()  # 显示

    def savefile(self,path):
        save_file=open(path,"wb")
        for line in  self.savelist:
            save_file.write(line.encode("utf-8"))
        save_file.close()





path="C:\\Users\\Tsinghua-yincheng\\Desktop\\tools\\csdn.txt"
#bigfind=BigdataSearchDisk(path,Outputview.OutputViewText.OutputViewText)
bigfind=BigdataSearchDisk(path,OuputViewList.OutputViewList)
#bigfind=BigdataSearchDisk(path,OutputViewTable.OutputViewTable,
                      #tableheadlist=["user","password","email"],splitstr=" # ")

bigfind.find("@163.com")
bigfind.savefile("1.txt")



