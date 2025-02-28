# 这个错误通常是因为数据中存在NaN（Not a Number）值，而MySQL无法直接插入这些值。要解决这个问题，可以先处理NaN值，将其转换为NULL或其他适当的默认值。

# 解决步骤
# 检查数据框中的 NaN 值：

# 使用pandas的功能来识别和处理NaN值。
# 转换 NaN 为NULL：

# 在将数据插入数据库之前，用pandas将NaN值替换为None，这样它们会作为NULL插入 MySQL 。
# 示例代码
# 假设我们有一个 DataFrame df，可以使用以下代码处理NaN值：

import pandas as pd
import pymysql
import os

# 读取 Excel 文件并处理 NaN 值
df = pd.read_excel(file_path)
df = df.where(pd.notnull(df), None)  # 将 NaN 替换为 None

# 创建 MySQL 连接
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
    with connection.cursor() as cursor:
        # 插入数据的 SQL 语句
        insert_sql = """
        INSERT INTO douyin_对标账号 (
            blogger, url, awesome_id, title, comment_count, share_count, 
            like_count, favorite_count, video_publish_time, collect_time, brand_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        # 准备数据插入
        data_to_insert = [
            (*row, brand_id) for row in df.itertuples(index=False, name=None)
        ]
        cursor.executemany(insert_sql, data_to_insert)
        print('数据插入成功！')

finally:
    connection.close()