# 批量创建表

import pymysql

# 数据库连接信息
connection = pymysql.connect(
    host='192.3.211.151',        # 替换为您的 MySQL 服务器地址
    user='root',                 # 替换为您的用户名
    password='123456',           # 替换为您的密码
    database='FZDB',             # 使用已创建的 FZDB 数据库
    charset='utf8mb4',
    port=3307,
    autocommit=True
)

# 要创建的表名列表
table_names = [
    "S&W_Marketing",

]

# 创建表的 SQL 模板
create_table_sql_template = """
CREATE TABLE IF NOT EXISTS `{table_name}` (
    `ID` INT AUTO_INCREMENT PRIMARY KEY,
    `Template` TEXT,
    `Template_Class` VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

try:
    with connection.cursor() as cursor:
        for table_name in table_names:
            create_table_sql = create_table_sql_template.format(table_name=table_name)
            cursor.execute(create_table_sql)
            print(f"Table {table_name} created successfully.")
finally:
    connection.close()


'''

表名为英文，单词间使用下划线链接
日常话题：Daily_Topics
风格话题：Style_Topics
场景话题：Scene_Topics
功能话题：Function_Topics
好物话题：Good_Finds_Topics
个性话题：Personality_Topics
我希望批量使用 pymysql 创建表名并定义字段，每个表的字段都是一致的：ID，模版内容，模版分类
下面是数据库信息，
connection = pymysql.connect(
host='192.3.211.151', # 替换为您的 MySQL 服务器地址
user='root', # 替换为您的用户名
password='123456', # 替换为您的密码
database='FZDB', # 使用已创建的 FZDB 数据库
charset='utf8mb4',
port=3307,
autocommit=True
)请实现需求
'''