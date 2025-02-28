# 顺序，这个表中查这个字段

import pymysql

def query_products_by_brand_id(brand_id):
    # 创建 MySQL 连接
    connection = pymysql.connect(
        host='192.3.211.151',  # 替换为您的 MySQL 服务器地址
        user='root',  # 替换为您的用户名
        password='123456',  # 替换为您的密码
        database='FZDB',  # 使用 FZDB 数据库
        charset='utf8mb4',
        port=3307
    )

    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 构建查询语句
        query = "SELECT * FROM brands_product WHERE brand_id = %s"

        # 执行查询
        cursor.execute(query, (brand_id,))

        # 获取查询结果
        results = cursor.fetchall()

        if results:
            for row in results:
                print(row)
        else:
            print("未找到相关产品信息")

    finally:
        # 关闭游标和连接
        cursor.close()
        connection.close()

if __name__ == "__main__":
    brand_id = 1  # 替换为您要查询的 brand_id 值
    query_products_by_brand_id(brand_id)