'''
我现在需要将本地的一个 json 文件通过链接在数据库中创建一个表 Product_Color，内容是单条数据示例： {
"Product_Color": "冰川白"
},
，我希望主键是 ID，自增，外键 Card 与 brands_product 表中的 Product_ID 为 1 的数据绑定
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

    # 创建表 Product_Color
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Product_Color (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Product_Color VARCHAR(255),
        Tag VARCHAR(255),  # 添加 tag 字段
        Card INT,
        FOREIGN KEY (Card) REFERENCES brands_product(Product_ID)
    )
    """
    cursor.execute(create_table_query)

    # 读取本地 JSON 文件
    with open('产品颜色.json', 'r') as f:
        data = json.load(f)

    # 遍历数据列表并插入到 Product_Color 表
    insert_query = "INSERT INTO Product_Color (Product_Color, Tag, Card) VALUES (%s, %s, 1)"  # 修改插入语句，包含 tag 字段
    for item in data:
        cursor.execute(insert_query, (item['Product_Color'], '颜色'))  # 为 tag 字段赋值为'颜色'

    # 关闭游标和连接
    cursor.close()
    connection.close()


import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

update_brand()