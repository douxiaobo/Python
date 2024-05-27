import pymysql

# 使用字典来传递连接参数
connection_params = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'db': 'testdb',
    'charset': 'utf8'
}

# 使用字典创建连接
db = pymysql.connect(**connection_params)

cursor=db.cursor()
cursor.execute("select version()")
data=cursor.fetchone()
print("Database version: %s" % data)

cursor.close()
db.close()


# douxiaobo@192 connectmysql % python3 -m venv pymysql
# douxiaobo@192 connectmysql % source pymysql/bin/activate
# (pymysql) douxiaobo@192 connectmysql % pip3 install pymysql
# Collecting pymysql
#   Downloading PyMySQL-1.1.1-py3-none-any.whl.metadata (4.4 kB)
# Downloading PyMySQL-1.1.1-py3-none-any.whl (44 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.0/45.0 kB 234.1 kB/s eta 0:00:00
# Installing collected packages: pymysql
# Successfully installed pymysql-1.1.1
# (pymysql) douxiaobo@192 connectmysql % 

#写代码失败了

# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/connectmysql/connectmysql.py", line 13, in <module>
#     db = pymysql.connect(**connection_params)
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/connectmysql/pymysql/lib/python3.12/site-packages/pymysql/connections.py", line 361, in __init__
#     self.connect()
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/connectmysql/pymysql/lib/python3.12/site-packages/pymysql/connections.py", line 669, in connect
#     self._request_authentication()
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/connectmysql/pymysql/lib/python3.12/site-packages/pymysql/connections.py", line 971, in _request_authentication
#     auth_packet = self._process_auth(plugin_name, auth_packet)
#                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/connectmysql/pymysql/lib/python3.12/site-packages/pymysql/connections.py", line 1062, in _process_auth
#     pkt = self._read_packet()
#           ^^^^^^^^^^^^^^^^^^^
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/connectmysql/pymysql/lib/python3.12/site-packages/pymysql/connections.py", line 775, in _read_packet
#     packet.raise_for_error()
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/connectmysql/pymysql/lib/python3.12/site-packages/pymysql/protocol.py", line 219, in raise_for_error
#     err.raise_mysql_exception(self._data)
#   File "/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/connectmysql/pymysql/lib/python3.12/site-packages/pymysql/err.py", line 150, in raise_mysql_exception
#     raise errorclass(errno, errval)
# pymysql.err.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: YES)")

# success
# python3 connectmysql.py
# Database version: 8.3.0
