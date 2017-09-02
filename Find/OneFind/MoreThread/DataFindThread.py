import threading

import Find.OneFind.OneFindBase
import Find.OneFind.MoreThread.findthread

class BigdataSearchThread(Find.OneFind.OneFindBase.OneSearch):
    def __init__(self, filepath, showtype, **arg):  # 兼容多个参数
        super().__init__(filepath, showtype, **arg)

    def find(self,findstr,Threadnum=10):
        self.mutex = threading.Lock()  # 线程锁
        self.alllist = []  # 保存所有的结果
        kaifanglist = self.file.readlines()  # 全部读入内存
        lineslength = len(kaifanglist)  # 全部的长度
        self.threadlist=[] #线程的列表

        N = Threadnum  # 线程的数量
        for i in range(N - 1):  # 0,9  不包含9.0,12,3,4,5,6,7,8
            mythd = find.morethread.FindThread.Find(kaifanglist,
                                                    i * (lineslength // (N - 1)),
                                                    (i + 1) * (lineslength // (N - 1)),
                                                    findstr,
                                                    self.mutex,
                                                    self.alllist)
            mythd.start()
            self.threadlist.append(mythd)

        mylastthd = find.morethread.FindThread.Find(kaifanglist,
                                                    lineslength // (N - 1) * (N - 1),
                                                    lineslength,
                                                    findstr,
                                                    self.mutex,
                                                    self.alllist)
        mylastthd.start()
        self.threadlist.append(mylastthd)

        for thd in self.threadlist:
            thd.join()
        print("搜索完成")
        for  line  in self.alllist:#图形界面上
            self.showwindow.adddata(line)  # 多态
        self.showwindow.show()  # 显示

    def savefile(self,path):
        save_file = open(path, "wb")
        for line in self.alllist:
            save_file.write(line.encode("utf-8"))
        save_file.close()