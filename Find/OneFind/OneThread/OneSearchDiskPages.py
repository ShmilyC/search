import Find.OneFind.OneFindBase

import OutputView.MorePage.OutputViewTextMorePage
import OutputView.MorePage.OutputViewListMorePage
import OutputView.MorePage.OutputViewTableMorePage


class OneSearchDiskPages(object):
    def __init__(self, filepath): # ,showtype,**kwargs
        self.file = open(filepath, 'rb')
        # self.showwindow = showtype

    def __del__(self):
        self.file.close()

    def find(self, findstr):
        self.savelist = []
        while True:
            line = self.file.readline()
            line = line.decode('gbk','ignore')
            if not line:
                break
            if line.find(findstr) != -1:
                print(line)
                self.savelist.append(line)
        alllist = []
        N = 100
        if len(self.savelist)%N == 0:
            mylist = []
            for i in range(len(self.savelist)):
                mylist.append(self.savelist[i])
                if i % 100 == 0:
                    mylist.append(mylist)
                    mylist = []
        else:
            mylist = []
            for i in range(len(self.savelist)):
                mylist.append(self.savelist[i])
                if i % 100 == 0 or i == len(self.savelist) - 1:
                    alllist.append(mylist)
                    mylist = []
        alllist.reverse()

        my = OutputView.MorePage.OutputViewListMorePage.OutputViewListPages(alllist)
        my.show()

path = 'E:\Python\learning\大数据相关数据\csdn1.txt'
my = OneSearchDiskPages(path)
my.find("@163.com")