'''
更新产品卡片名
目标表：brands_product
表字段：
Product_ID
int
Product_Number
varchar(255)
Product_Name
varchar(255)
brand_id
int

'''

import pymysql

# 数据库连接
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
        # 查询当前记录数量
        cursor.execute("SELECT COUNT(*) FROM brands_product")
        result = cursor.fetchone()  # 获取结果
        current_count = result[0] if result else 0

        # 下一个 Product_ID 为当前记录数量+1
        next_product_id = current_count + 1

        # SQL 插入语句
        sql = """
        INSERT INTO brands_product (Product_ID, Product_Number, Product_Name, brand_id)
        VALUES (%s, %s, %s, %s)
        """
        # 数据，注意这里的 Product_Number 和 Product_Name 是字符串，brand_id 是整型
        data = (next_product_id, 'S2AW8458', '后开扣运动内衣', 1)
        
        # 执行 SQL，并传入数据
        cursor.execute(sql, data)
        connection.commit()  # 提交事务

        print("数据插入成功! Product_ID 为:", next_product_id)

finally:
    connection.close()  # 确保关闭连接