import pymysql

# 连接 MySQL 服务器
db = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    charset='utf8'
    cursorclass=pymysql.cursors.DictCursor
)

# 创建数据库
with db.cursor() as cursor:
    sql_create_db = "CREATE DATABASE IF NOT EXISTS testdb;"
    cursor.execute(sql_create_db)
    db.commit()

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
#数据库操作语句
sql = """CREATE TABLE EMPLOYEETEST (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
#执行SQL语句
cursor.execute(sql)
#关闭数据库连接
cursor.close()
db.close()


# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/createmysqltable/run.py", line 3, in <module>
#     db = pymysql.connect(
#          ^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/createmysqltable/pymysql/lib/python3.12/site-packages/pymysql/connections.py", line 361, in __init__
#     self.connect()
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/createmysqltable/pymysql/lib/python3.12/site-packages/pymysql/connections.py", line 669, in connect
#     self._request_authentication()
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/createmysqltable/pymysql/lib/python3.12/site-packages/pymysql/connections.py", line 971, in _request_authentication
#     auth_packet = self._process_auth(plugin_name, auth_packet)
#                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/createmysqltable/pymysql/lib/python3.12/site-packages/pymysql/connections.py", line 1062, in _process_auth
#     pkt = self._read_packet()
#           ^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/createmysqltable/pymysql/lib/python3.12/site-packages/pymysql/connections.py", line 775, in _read_packet
#     packet.raise_for_error()
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/createmysqltable/pymysql/lib/python3.12/site-packages/pymysql/protocol.py", line 219, in raise_for_error
#     err.raise_mysql_exception(self._data)
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/createmysqltable/pymysql/lib/python3.12/site-packages/pymysql/err.py", line 150, in raise_mysql_exception
#     raise errorclass(errno, errval)
# pymysql.err.OperationalError: (1049, "Unknown database 'testdb'")
