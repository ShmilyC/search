import OutputView.OnePage.OutputViewTable
import OutputView.OnePage.OutputViewList
import OutputView.OnePage.OutputViewText

import Find.OneFind.OneFindBase

class OneSearchMEM(Find.OneFind.OneFindBase.OneSearch):
    def __init__(self,filepath,showtype,**kwargs):
        super().__init__(filepath,showtype,**kwargs)

    def find(self,findstr):
        self.savelist2 = []
        mydatalist = self.file.readlines()
        for line in mydatalist:
            line = line.decode('gbk','ignore')
            if line.find(findstr) != -1:
                print(line)
                self.savelist2.append(line)
                self.showwindow.adddata(line)
        self.showwindow.show()

    def savefile(self,path):
        save_file = open(path,'wb')
        for line in self.savelist2:
            save_file.write(line.encode('utf-8'))
            save_file.close()


# path='E:\Python\learning\大数据相关数据\csdn.txt'
# bigfind=OneSearchMEM(path,OutputView.OnePage.OutputViewTable.OutputViewTable,
#                   tableheadlist=["user","password","email"],splitstr=" # ")
#
# bigfind.find("3@163.com")