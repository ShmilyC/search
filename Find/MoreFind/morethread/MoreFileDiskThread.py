import Find.MoreFind.morefindbase

import OutputView.OnePage.OutputViewText
import OutputView.OnePage.OutputViewTable
import OutputView.OnePage.OutputViewList
import threading
import Find.MoreFind.morethread.disk_thread

class MoreFileFind_Disk(Find.MoreFind.morefindbase.MoreFileFind_Base):
    def __init__(self,filepathlist):
        super().__init__(filepathlist)
        self.mutex=threading.Lock() #锁

    def find(self,findstr,N=4):
        N=len(self.filelist)#每个文件开启一个线程
        threadlist=[]
        for  i  in range(N):
            mythd= Find.MoreFind.morethread.disk_thread.Disk_Thread(
                self.filelist[i],
                findstr,
                self.mutex,
                self.lastlist #创建一个线程
            )
            mythd.start()
            threadlist.append(mythd)
        for  thd  in threadlist:
            thd.join()
        print("搜索完成")