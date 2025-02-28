'''

'''
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

    # 创建游标
    cursor = connection.cursor()

    # 创建表 Product_DesignTagline
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Product_DesignTagline (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Product_DesignTagline VARCHAR(255),
        Tag VARCHAR(255),  # 添加 tag 字段
        Card INT,
        FOREIGN KEY (Card) REFERENCES brands_product(Product_ID)
    )
    """
    cursor.execute(create_table_query)

    # 读取本地 JSON 文件
    with open('设计宣传.json', 'r') as f:
        data = json.load(f)

    # 遍历数据列表并插入到 Product_DesignTagline 表
    insert_query = "INSERT INTO Product_DesignTagline (Product_DesignTagline, Tag, Card) VALUES (%s, %s, 1)"  # 修改插入语句，包含 tag 字段
    for item in data:
        cursor.execute(insert_query, (item['Product_DesignTagline'], item['Tag']))  # 为 tag 字段赋值为'颜色'

    # 关闭游标和连接
    cursor.close()
    connection.close()


import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

update_brand()