'''

还要增加一个字段

我需要对 brands 表新增列类型，是字符串，并添加数据，添加逻辑是：只有 brand_id 为1 的数据填写为速惟，其他为空数据
'''
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

try:
    with connection.cursor() as cursor:
        # 步骤 1: 添加新列 'nick_name'
        # add_column_sql = "ALTER TABLE `brands` ADD COLUMN `nick_name` VARCHAR(255)"
        # cursor.execute(add_column_sql)
        # print("成功添加新列 'nick_name'。")

        # 步骤 2: 更新 brand_id 为 1 的行
        update_sql = "UPDATE `brands` SET `nick_name` = '速惟' WHERE `brand_id` = %s"
        cursor.execute(update_sql, (1,))
        # print("成功更新 brand_id 为 1 的行。")
        
        # # 步骤 3: 将其他行类型设置为空，如果它们的类型还不是空的
        # clear_other_sql = "UPDATE `brands` SET `nick_name` = NULL WHERE `brand_id` != %s"
        # cursor.execute(clear_other_sql, (1,))
        # print("成功将其他行的 'nick_name' 设置为空。")

finally:
    connection.close()