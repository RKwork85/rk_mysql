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
        Product_Name VARCHAR(255),
        Product_Number VARCHAR(255),
        brand_id INT,
        FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE ON UPDATE CASCADE
    )
    """
    cursor.execute(create_table_query)

    # 插入数据
    insert_query = """
    INSERT INTO brands_product (ID, Product_Name, Product_Number, brand_id)
    VALUES (%s, %s, %s, %s)
    """
    for item in data:
        cursor.execute(insert_query, (item['ID'], item['Product_Name'], item['Product_Number'], 1))

    # 关闭游标和连接
    cursor.close()
    connection.close()

if __name__ == "__main__":
    update_brand()