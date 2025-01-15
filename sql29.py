'''
删除表字段为某ID的数据
'''

import pymysql

# 数据库连接配置
connection = pymysql.connect(
    host='192.3.211.151',
    user='root',
    password='123456',
    database='FZDB',
    charset='utf8mb4',
    port=3307,
    autocommit=True
)

try:
    # 创建游标对象
    with connection.cursor() as cursor:
        # 定义要删除的 Card 值列表
        card_values = [2, 3]  # 假设你要删除的 Card 值有 2, 3, 5
        
        # 构建 SQL 删除语句，使用 %s 占位符
        sql_delete_query = "DELETE FROM brands_product WHERE Product_ID IN (%s)" % ','.join(['%s'] * len(card_values))
        # DELETE FROM Product_Color WHERE Card IN (%s,%s)
        print(sql_delete_query)
        
        # 执行 SQL 删除语句，传入多个值
        cursor.execute(sql_delete_query, tuple(card_values))
        
        # 提交更改
        connection.commit()
        
        # 打印删除的记录数
        print(f"Deleted {cursor.rowcount} record(s) with Card values {card_values}.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 关闭数据库连接
    connection.close()