import pymysql

# 建立连接
connection = pymysql.connect(
    host='192.3.211.151',  
    user='root',  
    password='123456',  
    database='FZDB',  
    charset='utf8mb4',
    port=3307,
    autocommit=True
)

try:
    with connection.cursor() as cursor:
        # SQL 查询
        sql = "SELECT Template FROM `S&W_Marketing`;"
        cursor.execute(sql)
        
        # 获取结果
        results = cursor.fetchall()
        print(results)
        # 打印结果
        for row in results:
            print(row[0])  # row[0] 是 Template 列的值
finally:
    connection.close()