import threading

class  Disk_Thread(threading.Thread):
    def __init__(self,file,findstr,mutex,lastlist):#文件，查找的字符串，锁，保存结果list
        super().__init__()
        self.file=file
        self.findstr=findstr
        self.mutex=mutex
        self.lastlist=lastlist
    def run(self):
        self.findlist=[]
        while True:
            line=self.file.readline()
            if not line:
                break
            line =line.decode("gbk","ignore")
            if line.find(self.findstr)!=-1:
                print(self.getName(),line)
                self.findlist.append(line) #保存

        with self.mutex:#信号量
            self.lastlist.append(self.findlist) #收集结果
