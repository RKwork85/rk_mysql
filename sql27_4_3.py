import pymysql
import os
import json
from concurrent.futures import ThreadPoolExecutor

def insert_product_data(dataJson, connection_params):
    # 创建一个新的数据库连接
    connection = pymysql.connect(**connection_params)
    
    with connection.cursor() as cursor:
        # 插入产品信息
        sql_cardInfo = """
        INSERT INTO brands_product (Product_Number, Product_Name, brand_id)
        VALUES (%s, %s, %s)
        """
        data = (dataJson['货号'][0], dataJson['产品名'][0], 1)
        cursor.execute(sql_cardInfo, data)
        
        # 获取 插入后的 Product_ID
        next_product_id = cursor.lastrowid

        # 插入颜色信息
        insertColor = """
        INSERT INTO Product_Color(Product_ID, Product_Color, Tag, Card)
        VALUES(%s, %s, %s, %s)
        """
        for index, color in enumerate(dataJson['颜色']):
            data = (next_product_id, color, "颜色", next_product_id)
            cursor.execute(insertColor, data)

        # 插入其它信息
        insert_data_into_table(cursor, "Product_DesignTagline", "设计宣传", dataJson['设计宣传'], next_product_id)
        insert_data_into_table(cursor, "Product_FabDescription", "FAB 产品解说", dataJson['FAB 产品解说'], next_product_id)
        insert_data_into_table(cursor, "Product_FabricDescription", "面料解说", dataJson['面料解说'], next_product_id)
        insert_data_into_table(cursor, "Product_FabricTagline", "面料宣传", dataJson['面料宣传'], next_product_id)
        insert_data_into_table(cursor, "Product_Process", "工艺", dataJson['工艺'], next_product_id)
        insert_data_into_table(cursor, "Product_SportScenes", "运动场景", dataJson['运动场景'], next_product_id)
        insert_data_into_table(cursor, "Product_Tagline", "一句话宣传", dataJson['一句话宣传'], next_product_id)
        insert_data_into_table(cursor, "Product_UserPainPoints", "用户痛点", dataJson['用户痛点'], next_product_id)
        insert_data_into_table(cursor, "Product_PatternTagline", "版型宣传", dataJson['版型宣传'], next_product_id)

        connection.commit()  # 提交事务
        print("数据插入成功! Product_ID 为:", next_product_id)

    connection.close()  # 关闭连接

def insert_data_into_table(cursor, table_name, tag, data_list, CardId):
    insert_sql = f'''
    INSERT INTO {table_name}(Product_ID, {table_name}, Tag, Card)
    VALUES(%s, %s, %s, %s)
    '''
    for index, value in enumerate(data_list):
        data = (CardId, value, tag, CardId)
        cursor.execute(insert_sql, data)

def main():
    # 数据库连接参数
    connection_params = {
        'host': '192.3.211.151',
        'user': 'root',
        'password': '123456',
        'database': 'FZDB',
        'charset': 'utf8mb4',
        'port': 3307,
        'autocommit': True  # 设置为自动提交
    }

    filePath = './inputCardInfo.json'  # JSON 文件所在文件夹
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            dataJsonList = json.load(file)  # 加载所有数据
            with ThreadPoolExecutor(max_workers=5) as executor:  # 线程池，最大 5个线程
                executor.map(lambda data: insert_product_data(data, connection_params), dataJsonList)

    except Exception as e:
        print(f"出错了: {e}")

if __name__ == '__main__':
    main()