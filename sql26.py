import json
import pymysql

# 数据库连接信息
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
        # 读取 JSON 文件
        with open('好物话题.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Insert 数据到 Scene_Topics 表
        insert_query = """
            INSERT INTO Good_Finds_Topics (ID, Template, Template_Class)
            VALUES (%s, %s, %s)
        """

        for item in data:
            # 提取每条记录的数据
            record_id = item['ID']
            template = item['文案模版']
            template_class = item['话题分类']
            
            # 执行 SQL 插入操作
            cursor.execute(insert_query, (record_id, template, template_class))

finally:
    connection.close()