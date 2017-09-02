import threading

class Find(threading.Thread):
    def __init__(self,linelist,istart,iend,searchstr,mutex,allsavelist):
        super().__init__()
        self.linelist = linelist  # 共享的list
        self.istart = istart  # 开始
        self.iend = iend  # 结束
        self.searchstr = searchstr  # 要查找
        self.findlist = []  # 保存结果
        self.mutex = mutex  # 互排斥锁
        self.allsavelist = allsavelist  # 保存

    def run(self):
        for i in range(self.istart,self.iend):
            line = self.linelist[i].decode('gbk','ignore')
            if line.find(self.searchstr)!=-1:
                print(self.getName(), line, end="")  # 标记谁找到的
                self.findlist.append(line)  # 找到的结果保存到列表

        with self.mutex: #线程安全，每个时刻，仅有一个线程访问
            for line in  self.findlist:#批量写入
                self.allsavelist.extend(self.findlist)#拓展