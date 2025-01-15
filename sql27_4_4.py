'''
目标表是 brands_product，你想要根据其主键值查找并删除所有与其相关的外键数据，然后删除目标表中的该条记录。

实现卡片表信息的批量化删除
'''
import pymysql

def delete_related_brands_products(product_ids):
    # 创建 MySQL 连接
    connection = pymysql.connect(
        host='192.3.211.151',
        user='root',
        password='123456',
        database='FZDB',
        charset='utf8mb4',
        port=3307,
        autocommit=False  # 使用事务
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

            # 遍历每个产品 ID
            for product_id in product_ids:
                # 删除所有引用该产品 ID 的记录
                for (table_name, column_name) in foreign_keys:
                    delete_query = f"DELETE FROM {table_name} WHERE {column_name} = %s"
                    cursor.execute(delete_query, (product_id,))
                    print("--删除--", table_name, "--列--", column_name, "--产品 ID--", product_id)
                
                # 删除 `brands_product` 表中的记录
                delete_product_query = "DELETE FROM brands_product WHERE Product_ID = %s"
                cursor.execute(delete_product_query, (product_id,))
            
            connection.commit()
            print(f"Deleted products {product_ids} and their related entries")

    except Exception as e:
        connection.rollback()
        print(f"An error occurred: {e}")

    finally:
        connection.close()

# 示例用法
delete_related_brands_products([8,9])  # 替换为你要删除的实际产品 ID 列表