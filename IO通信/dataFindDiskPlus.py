import time
import queue
import threading
import getandshow
import DataFindBase
import OuputViewList

class SearchDiskPlus(DataFindBase.BigdataSearch):
    def __init__(self,filepath,showtype,**kwargs):
        super().__init__(self,filepath,showtype,**kwargs)
        self.queue = queue.Queue(100)
        
    def findgo(self,findstr):
        self.addthrread = getandshow.AddDataThread(self.showwindow,self.queue)
        self.addthrread.start()
        self.findthread = threading.Thread(target=self.find,args=(findstr,))
        self.findthread.start()
        
        self.showwindow.show()
        
    def find(self,findstr):
        self.savelist = []
        while True:
            line = self.file.readline()
            line = line.decode('gbk','ignore')
            if not line:
                break
            if line.find(findstr) != -1:
                print(line)
                self.queue.put(line)
                self.savelist.append(line)
                time.sleep(1)
                
    def savefile(self,path):
        save_file = open(path,'wb')
        for line in self.savelist:
            save_file.write(line.encode('utf-8'))
        save_file.close()
        
