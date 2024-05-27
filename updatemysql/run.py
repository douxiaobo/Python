import pymysql
# 打开数据库连接
db = pymysql.connect(
    host="localhost",
    user="root",
    password="85Dxb1020.",
    db="testdb",
    charset='utf8'
)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 更新语句,AGE+2
sql = "UPDATE EMPLOYEE SET AGE = AGE + 2 WHERE SEX = '%c'" % ('M')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
# 关闭数据库连接
db.close()

# douxiaobo@192 updatemysql % python3 -m venv pymysql
# douxiaobo@192 updatemysql % source pymysql/bin/activate
# (pymysql) douxiaobo@192 updatemysql % pip3 install pymysql
# Collecting pymysql
#   Using cached PyMySQL-1.1.1-py3-none-any.whl.metadata (4.4 kB)
# Using cached PyMySQL-1.1.1-py3-none-any.whl (44 kB)
# Installing collected packages: pymysql
# Successfully installed pymysql-1.1.1
# (pymysql) douxiaobo@192 updatemysql % python3 run.py
# (pymysql) douxiaobo@192 updatemysql % 