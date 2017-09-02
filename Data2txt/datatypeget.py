import Data2txt.otherfilefind.csv2txt
class  datatypeGet(object):
    def __init__(self):
        self.mycsv=Data2txt.otherfilefind.csv2txt.csvtotxt() #创建csv处理对象

    def check(self,path):
        #path="C:\Users\Tsinghua-yincheng\Desktop\tools\1.txt"
        filetype=path[-5:]
        if filetype.find(".txt")!=-1:
            return path  #返回原来的路径
        elif filetype.find(".csv")!=-1:
            return   self.mycsv.getnewpath(path)
        elif filetype.find(".doc")!=-1:
            pass
        elif filetype.find(".docx")!=-1:
            pass
        elif filetype.find(".pdf")!=-1:
            pass
        elif filetype.find(".xls")!=-1:
            pass
        elif filetype.find(".xlsx")!=-1:
            pass
        elif filetype.find(".sql")!=-1:
            pass
        elif filetype.find(".bak")!=-1:
            pass
        elif filetype.find(".mdb")!=-1:
            pass
        elif filetype.find(".MDF")!=-1:
            pass
        else:
            pass