## 查表某表数据条数

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
        # 查询数据条数
        count_query = "SELECT COUNT(*) FROM `Daily_Topics`"
        cursor.execute(count_query)
        
        # 获取查询结果
        result = cursor.fetchone()
        count = result[0]  # 获取计数值
        
        print(f"Daily_Topics 表中共有 {count} 条数据。")
finally:
    connection.close()