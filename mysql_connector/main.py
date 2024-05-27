import mysql.connector      # brew install mysql-connector-python
 
# 连接到MySQL数据库
config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'MySql',
  'raise_on_warnings': True
}
 
try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
 
    # 执行一个查询
    query = "SELECT * FROM your_table"
    cursor.execute(query)
 
    # 获取查询结果
    records = cursor.fetchall()
    for row in records:
        print(row)
 
except mysql.connector.Error as error:
    print("Failed to connect to database: {}".format(error))
 
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")