import pymysql
#连接数据库
db = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="testdb",
    charset='utf8'
)
#获取操作游标
cursor = db.cursor()
# SQL 插入语句
sql = """INSERT INTO EMPLOYEETEST(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   db.rollback()  # 发生错误时回滚
# 关闭数据库连接
db.close()