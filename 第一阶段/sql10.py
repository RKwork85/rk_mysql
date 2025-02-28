## 查询外键关系
import pymysql

def get_table_relationships(db_name):
    connection = pymysql.connect(
        host='192.3.211.151',  
        user='root',  
        password='123456',  
        database=db_name,  
        charset='utf8mb4',
        port=3307,
        autocommit=True
    )

    try:
        with connection.cursor() as cursor:
            # 查询 INFORMATION_SCHEMA.KEY_COLUMN_USAGE 表以获取外键信息
            query = """
            SELECT 
                TABLE_SCHEMA, 
                TABLE_NAME, 
                COLUMN_NAME, 
                REFERENCED_TABLE_SCHEMA, 
                REFERENCED_TABLE_NAME, 
                REFERENCED_COLUMN_NAME
            FROM
                INFORMATION_SCHEMA.KEY_COLUMN_USAGE
            WHERE
                REFERENCED_TABLE_SCHEMA IS NOT NULL 
                AND TABLE_SCHEMA = %s;
            """
            cursor.execute(query, (db_name,))
            relationships = cursor.fetchall()
            return relationships
    finally:
        connection.close()

if __name__ == '__main__':
    db_name = 'FZDB'  # 替换为您的数据库名称
    relationships = get_table_relationships(db_name)
    for rel in relationships:
        print(rel)


# ('FZDB', 'douyin_target_accounts', 'brand_id', 'FZDB', 'brands', 'brand_id')
# ('FZDB', 'orders', 'user_id', 'FZDB', 'users', 'user_id')