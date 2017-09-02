import multiprocessing
import os
#搜索kaifang,开始，结束，查找的字符串，lastlist保存结果
class  ProcessFind:
    def  findkaifang(kaifanglist,istart,iend,searchstr,lastlist):
        for i in range(istart,iend):
            line=kaifanglist[i].decode("gbk","ignore")
            if  line.find(searchstr)!=-1:
                print(os.getpid(),line) #那个进程找到的
                lastlist.append(line) #保存结果
