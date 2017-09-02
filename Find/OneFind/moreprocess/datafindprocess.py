import multiprocessing

import Find.OneFind.moreprocess.findprocess

class BigdataSearchGeventProcess:
    def __init__(self,filepath,showtype,**arg):#兼容多个参数
        self.file=open(filepath,"rb")
        self.showwindow=showtype(**arg)

    def __del__(self):
        self.file.close()

    def find(self,findstr,N=3): #默认3个进程
        self.kaifanglist = multiprocessing.Manager().list()  # 共享内存。查询
        self.lastlist = multiprocessing.Manager().list()  # 结果
        self.kaifanglist.extend(self.file.readlines()) #加载内容到内存
        lines=len(self.kaifanglist)#长度
        processlist = []  # 进程列表

        for i in range(N - 1):
            process = multiprocessing.Process(target=find.moreProcess.Findprocess.ProcessFind.findkaifang,
                                              args=(self.kaifanglist,
                                                    i * (lines // (N - 1)),
                                                    (i + 1) * (lines // (N - 1)),
                                                    findstr,
                                                    self.lastlist))
            process.start()
            processlist.append(process)  # 加入进程列表
        mylastprocess = multiprocessing.Process(target=find.moreProcess.Findprocess.ProcessFind.findkaifang,
                                                args=(self.kaifanglist,
                                                      lines // (N - 1) * (N - 1),
                                                      lines,
                                                      findstr,
                                                      self.lastlist))
        mylastprocess.start()
        processlist.append(mylastprocess)

        for process in processlist:
            process.join()
        print("搜索完成")
        for  line  in self.lastlist:#图形界面上
            self.showwindow.adddata(line)  # 多态
        self.showwindow.show()  # 显示

    def savefile(self,path):
        save_file = open(path, "wb")
        for line in self.lastlist:
            save_file.write(line.encode("utf-8"))
        save_file.close()