'''
目标表是 brands_product，你想要根据其主键值查找并删除所有与其相关的外键数据，然后删除目标表中的该条记录。

实现卡片表信息的批量化删除
'''
import pymysql

def delete_related_brands_product(product_id):
    # 创建 MySQL 连接
    connection = pymysql.connect(
        host='192.3.211.151',
        user='root',
        password='123456',
        database='FZDB',
        charset='utf8mb4',
        port=3307,
        autocommit=False  # Use transactions
    )

    try:
        with connection.cursor() as cursor:
            # 查找所有与 `brands_product` 表有关的外键关系
            query_fk = """
            SELECT TABLE_NAME, COLUMN_NAME
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
            WHERE REFERENCED_TABLE_NAME = 'brands_product' AND TABLE_SCHEMA = 'FZDB';
            """
            cursor.execute(query_fk)
            foreign_keys = cursor.fetchall()

            # 删除所有引用该产品 ID 的记录
            for (table_name, column_name) in foreign_keys:
                delete_query = f"DELETE FROM {table_name} WHERE {column_name} = %s"
                cursor.execute(delete_query, (product_id,))
                print("--table_name--" ,table_name,"--column_name", column_name)
            
            # 删除 `brands_product` 表中的记录
            delete_product_query = "DELETE FROM brands_product WHERE Product_ID = %s"
            cursor.execute(delete_product_query, (product_id,))
            
            connection.commit()
            print(f"Deleted product {product_id} and its related entries")

    except Exception as e:
        connection.rollback()
        print(f"An error occurred: {e}")

    finally:
        connection.close()

# Example usage
delete_related_brands_product(3)  # Replace `5` with the actual `Product_ID` you want to delete