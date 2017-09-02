import OutputView.OnePage.OutputViewText
import OutputView.OnePage.OutputViewList
import OutputView.OnePage.OutputViewTable

import Find.OneFind.OneFindBase

class OneSearchDisk(Find.OneFind.OneFindBase.OneSearch):
    def __init__(self,filepath,showtype,**kwargs):
        super().__init__(filepath,showtype,**kwargs)

    def find(self,findstr):
        self.savelist3 = []
        while True:
            line = self.file.readline()
            line = line.decode('gbk','ignore')
            if not line:
                break
            if line.find(findstr) != -1:
                print(line)
                self.savelist3.append(line)
                self.showwindow.adddata(line)
        self.showwindow.show()

    def savefile(self,path):
        save_file = open(path,'wb')
        for line in self.savelist3:
            save_file.write(line.encode('utf-8'))

        save_file.close()


# path='E:\Python\learning\大数据相关数据\csdn1.txt'
# bigfind=OneSearchDisk(path,OutputView.OnePage.OutputViewTable.OutputViewTable,
#                   tableheadlist=["user","password","email"],splitstr=" # ")
#
# bigfind.find("3@163.com")