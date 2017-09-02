import Find.OneFind.OneFindBase

import OutputView.MorePage.OutputViewTextMorePage
import OutputView.MorePage.OutputViewListMorePage
import OutputView.MorePage.OutputViewTableMorePage

class OneSearchMEMPages(object):
    def __init__(self,filepath):
        self.file = open(filepath,'rb')

    def __del__(self):
        self.file.close()

    def find(self,findstr):
        self.savelist = []
        linelist = self.file.readlines()
        for line in linelist:
            line = line.decode("gbk", "ignore")
            if line.find(findstr) != -1:#find
                print(line)
                self.savelist.append(line)
        alllist=[]
        N=100
        if  len(self.savelist)%N==0:
            mylist=[] #列表
            for  i  in range(len(self.savelist)):
                mylist.append(self.savelist[i])
                if i%100==0:
                    alllist.append(mylist)
                    mylist=[]

        else:
            mylist = []  # 列表
            for i in range(len(self.savelist)):
                mylist.append(self.savelist[i])
                if i % 100 == 0  or  i==len(self.savelist)-1:
                    alllist.append(mylist)
                    mylist = []
        alllist.reverse()
        #self.savelist  =787  700
        my = OutputView.MorePage.OutputViewListMorePage.OutputViewListPages(alllist)
        my.show()

# path = 'E:\Python\learning\大数据相关数据\csdn1.txt'
# my = OneSearchMEMPages(path)
# my.find("@163.com")