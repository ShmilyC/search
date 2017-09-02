import Find.MoreFind.morefindbase

import OutputView.OnePage.OutputViewText
import OutputView.OnePage.OutputViewTable
import OutputView.OnePage.OutputViewList


class MoreFileFind_Disk(Find.MoreFind.morefindbase.MoreFileFind_Base):
    def __init__(self,filepathlist):
        super().__init__(filepathlist)

    def find(self,findstr):
        for  file  in  self.filelist:
            filefindlist=[]
            while True:
                line=file.readline() #循环一个文件的每一行
                if not line: #如果为空就结束
                    break
                line=line.decode("gbk","ignore")
                if  line.find(findstr)!=-1:
                    filefindlist.append(line)
                    print(line)
            self.lastlist.append(filefindlist)#列表的列表添加一个列表
