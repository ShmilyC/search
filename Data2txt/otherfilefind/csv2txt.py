
import csv

class csvtotxt:
    def getnewpath(self,path):
        self.newpath=path[:-4]+".txt"
        file=open(self.newpath,"wb")
        reader = csv.reader(open("path", "r"))
        for item in reader:  # item读一行
            file.write(str(item).encode("utf-8"))#写入文本
        file.close()
        return self.newpath
