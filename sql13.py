# 逆序 这个一我懂，但是我希望通过 brands 表的外键关系查询到 brands_product 表中的相关信息

import pymysql

def query_products_by_brand_id(brand_id):
    # 创建 MySQL 连接
    connection = pymysql.connect(
        host='192.3.211.151',  
        user='root',  
        password='123456',  
        database='FZDB',  
        charset='utf8mb4',
        port=3307
    )

    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 构建查询语句，通过连接 brands 表和 brands_product 表来查询相关产品信息
        query = """
        SELECT bp.* 
        FROM brands_product bp
        JOIN brands b ON bp.brand_id = b.brand_id
        WHERE b.brand_id = %s
        """

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