class BigdataSearchGevent:
    def __init__(self, filepath, showtype, **arg):  # 兼容多个参数
        self.file = open(filepath, "rb")
        self.showwindow = showtype(**arg)

    def __del__(self):
        self.file.close()

    def find(self,findstr):
        pass