import pymysql

# 数据库连接信息
connection = pymysql.connect(
    host='192.3.211.151',        # 替换为您的 MySQL 服务器地址
    user='root',                 # 替换为您的用户名
    password='123456',           # 替换为您的密码
    database='FZDB',             # 使用已创建的 FZDB 数据库
    charset='utf8mb4',
    port=3307
)

try:
    # 创建游标对象
    with connection.cursor() as cursor:
        # 查询当前表中最大的 ID 值
        cursor.execute("SELECT MAX(ID) FROM Product_Color")
        max_id = cursor.fetchone()[0]  # 获取查询结果中的最大 ID 值
        
        # 如果表为空，max_id 为 None，设置初始值为 1
        if max_id is None:
            new_id = 1
        else:
            new_id = max_id + 1  # 新 ID 为当前最大 ID 加 1
        
        # 插入数据的 SQL 语句
        sql = """
        INSERT INTO Product_Color (ID, Product_Color, Tag, Card)
        VALUES (%s, %s, %s, %s)
        """
        # 数据值
        values = (new_id, '青柠绿', '颜色', 1)  # 新 ID，颜色为海沫绿，Tag 为新颜色，Card 为 1
        
        # 执行 SQL 语句
        cursor.execute(sql, values)
        # 提交事务
        connection.commit()
        print(f"数据插入成功！新记录的 ID 为 {new_id}")
except pymysql.MySQLError as e:
    print(f"插入数据失败：{e}")
finally:
    # 关闭数据库连接
    connection.close()



