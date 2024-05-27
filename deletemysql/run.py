import pymysql
# 打开数据库连接
db = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="testdb",
    charset='utf8'
)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
sql = "DELETE FROM EMPLOYEETEST WHERE AGE > %s" % (20)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
# 关闭数据库连接
db.close()