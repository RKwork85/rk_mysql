'''
设置主键自增逻辑
'''

import pymysql

# 数据库连接信息
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
        # 修改表结构，将 Product_ID 设置为自动递增并作为主键
        alter_table_sql = """
        ALTER TABLE brands_product
        MODIFY COLUMN Product_ID INT AUTO_INCREMENT PRIMARY KEY;
        """
        
        # 执行 SQL 语句
        cursor.execute(alter_table_sql)
        connection.commit()  # 提交更改
        print("表结构修改成功，Product_ID 已设置为自动递增并作为主键。")

finally:
    connection.close()  # 关闭数据库连接