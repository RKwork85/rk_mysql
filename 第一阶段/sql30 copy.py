import pymysql

# 数据库连接信息
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
        # 添加新列 Template_Name
        add_column_sql = """
        ALTER TABLE `S&W_Marketing`
        ADD COLUMN Template_Name VARCHAR(255);
        """
        cursor.execute(add_column_sql)

        # 更新 Template_Name 列的值
        update_column_sql = """
        UPDATE `S&W_Marketing`
        SET Template_Name = CONCAT('Bh', ID);
        """
        cursor.execute(update_column_sql)

    # 提交更改
    connection.commit()

finally:
    # 关闭连接
    connection.close()