# json文件创表
# 我有一个这样的 json 文件，我希望将 json 文件的数据创建到表中，并且每条数据关联 brands 表中的 brand_id 字段 为 1 作为外键


import json
import pymysql

def update_brand():
    # 创建 MySQL 连接
    connection = pymysql.connect(
        host='192.3.211.151',  # 替换为您的 MySQL 服务器地址
        user='root',  # 替换为您的用户名
        password='123456',  # 替换为您的密码
        database='FZDB',  # 使用 FZDB 数据库
        charset='utf8mb4',
        port=3307,
        autocommit=True
    )

    # 创建游标对象
    cursor = connection.cursor()

    # 假设您的 JSON 数据存储在一个文件中，读取该文件
    with open('产品信息.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 创建表（如果表不存在）
    create_table_query = """
    CREATE TABLE IF NOT EXISTS brands_product (
        ID INT PRIMARY KEY,
        产品名 VARCHAR(255),
        brand_id INT,
        FOREIGN KEY (brand_id) REFERENCES brands(brand_id)
    )
    """
    cursor.execute(create_table_query)

    # 插入数据
    insert_query = """
    INSERT INTO brands_product (ID, 产品名, brand_id)
    VALUES (%s, %s, %s)
    """
    for item in data:
        cursor.execute(insert_query, (item['ID'], item['产品名'], 1))

    # 关闭游标和连接
    cursor.close()
    connection.close()

if __name__ == "__main__":
    update_brand()