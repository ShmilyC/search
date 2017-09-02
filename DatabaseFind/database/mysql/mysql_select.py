import DatabaseFind.database_base
import pymysql
import OutputView.OnePage.OutputViewText
import OutputView.OnePage.OutputViewTable
import OutputView.OnePage.OutputViewList

class MySQL_Select(DatabaseFind.database_base.DataBase_Base):
    def __init__(self,ip,user,password,database,showtype):
        self.db = pymysql.connect(ip,user,password,database)
        self.win=showtype()
    def __del__(self):
        self.db.close()  # 关闭数据库
    def  find(self,findstr):
        cursor = self.db.cursor()  # 游标
        sqlstr = "select * from xiaomi_com where email like '%"+findstr+"%'"
        cursor.execute(sqlstr)  # 执行sQL语句
        res = cursor.fetchall()  # zh抓取返回结果
        for line in res:  # 显示数据
            print(line)
            self.win.adddata(line)
        self.win.show()



mysql=MySQL_Select("127.0.0.1", "root", "111111", "xiaomi", Outputview.OnePage.OuputViewList.OutputViewList)
mysql.find("yincheng")