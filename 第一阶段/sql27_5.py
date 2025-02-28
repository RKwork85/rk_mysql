'''
误删表
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

    # 创建游标对象
    cursor = connection.cursor()

    # 假设您的 JSON 数据存储在一个文件中，读取该文件
    with open('产品信息.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 创建表（如果表不存在）
    create_table_query = """
    CREATE TABLE IF NOT EXISTS brands_product (
        Product_ID INT AUTO_INCREMENT PRIMARY KEY,
        Product_Number VARCHAR(255),
        Product_Name VARCHAR(255),
        brand_id INT,
        FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE ON UPDATE CASCADE
    )
    """
    cursor.execute(create_table_query)

    # 插入数据
    insert_query = """
    INSERT INTO brands_product (Product_ID, Product_Number, Product_Name,  brand_id)
    VALUES (%s, %s, %s, %s)
    """
    for item in data:
        cursor.execute(insert_query, (item['ID'], item['Product_Number'], item['Product_Name'], 1))

    # 关闭游标和连接
    cursor.close()
    connection.close()

if __name__ == "__main__":
    update_brand()


# ALTER TABLE Product_Color 
# ADD CONSTRAINT Product_Color_ibfk_1 FOREIGN KEY (Card) REFERENCES brands_product(Product_ID);

# ALTER TABLE Product_DesignTagline 
# ADD CONSTRAINT Product_DesignTagline_ibfk_1 FOREIGN KEY (Card) REFERENCES brands_product(Product_ID);

# ALTER TABLE Product_FabDescription 
# ADD CONSTRAINT Product_FabDescription_ibfk_1 FOREIGN KEY (Card) REFERENCES brands_product(Product_ID);

# ALTER TABLE Product_FabricDescription 
# ADD CONSTRAINT Product_FabricDescription_ibfk_1 FOREIGN KEY (Card) REFERENCES brands_product(Product_ID);

# ALTER TABLE Product_FabricTagline 
# ADD CONSTRAINT Product_FabricTagline_ibfk_1 FOREIGN KEY (Card) REFERENCES brands_product(Product_ID);

# ALTER TABLE Product_Process 
# ADD CONSTRAINT Product_Process_ibfk_1 FOREIGN KEY (Card) REFERENCES brands_product(Product_ID);

# ALTER TABLE Product_SportScenes 
# ADD CONSTRAINT Product_SportScenes_ibfk_1 FOREIGN KEY (Card) REFERENCES brands_product(Product_ID);

# ALTER TABLE Product_Tagline 
# ADD CONSTRAINT Product_Tagline_ibfk_1 FOREIGN KEY (Card) REFERENCES brands_product(Product_ID);

# ALTER TABLE Product_UserPainPoints 
# ADD CONSTRAINT Product_UserPainPoints_ibfk_1 FOREIGN KEY (Card) REFERENCES brands_product(Product_ID);

# ALTER TABLE Product_patternTagline 