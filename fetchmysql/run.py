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
# SQL 查询语句
sql = "SELECT * FROM EMPLOYEETEST \
       WHERE INCOME > %s" % (1000)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()      # fetchone()方法获取单条数据，fetchall()方法获取所有数据
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # 打印结果
      print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income ))
except:
   print("Error: unable to fecth data")
# 关闭数据库连接
db.close()

# (pymysql) douxiaobo@192 fetchmysql % python3 run.py
# Error: unable to fecth data
# (pymysql) douxiaobo@192 fetchmysql % python3 run.py
# fname=Mac,lname=Mohan,age=20,sex=M,income=2000.0
# (pymysql) douxiaobo@192 fetchmysql % 