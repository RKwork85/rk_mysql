import pymysql

# 数据库连接信息
connection = pymysql.connect(
    host='192.3.211.151',        # 替换为您的 MySQL 服务器地址
    user='root',                 # 替换为您的用户名
    password='123456',           # 替换为您的密码
    database='FZDB',             # 使用已创建的 FZDB 数据库
    charset='utf8mb4',
    port=3307
)

try:
    with connection.cursor() as cursor:
        # 查询 ID 为 5 的数据
        query = "SELECT * FROM Daily_Topics WHERE ID = %s"
        cursor.execute(query, (5,))
        
        # 获取查询结果
        result = cursor.fetchone()  # 获取一条结果
        
        if result:
            print(f"ID: {result[0]}")
            print(f"模板内容: {result[1]}")
            print(f"模板分类: {result[2]}")
        else:
            print("没有找到 ID 为 5 的记录。")
finally:
    connection.close()