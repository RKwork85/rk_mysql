import pymysql

def column_exists(cursor, table_name, column_name):
    # 查询 information_schema 来检查列是否存在
    query = f"""
    SELECT COUNT(*)
    FROM information_schema.columns
    WHERE table_schema = DATABASE()
    AND table_name = '{table_name}'
    AND column_name = '{column_name}'
    """
    cursor.execute(query)
    # 返回结果 True or False
    return cursor.fetchone()[0] > 0

# 创建数据库连接
connection = pymysql.connect(
    host='192.3.211.151',
    user='root',
    password='123456',
    database='FZDB',
    charset='utf8mb4',
    port=3307
)

try:
    with connection.cursor() as cursor:
        table_name = 'brands_product'
        column_name = 'Product_Number'
        
        # 检查列是否存在
        if not column_exists(cursor, table_name, column_name):
            # 如果列不存在，则新增列
            add_column_query = f"""
                ALTER TABLE {table_name}
                ADD COLUMN {column_name} VARCHAR(255) AFTER Product_ID;
            """
            cursor.execute(add_column_query)
            print(f"Column '{column_name}' added.")
        else:
            print(f"Column '{column_name}' already exists.")
        
        # 更新数据，无论是否新增列都进行更新
        update_data_queries = [
            "UPDATE brands_product SET Product_Number = 'S4SS1067' WHERE Product_ID = 1;",
            "UPDATE brands_product SET Product_Number = 'S3AW1066' WHERE Product_ID = 2;"
        ]
        
        for query in update_data_queries:
            cursor.execute(query)

        # 提交更改以保存操作结果
        connection.commit()

finally:
    connection.close()