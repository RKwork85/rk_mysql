import pandas as pd
import pymysql

# 读取 Excel 文件
file_path = '/home/rkwork/rkwork/project/muzi_python/muzi_mysql/品牌表.xlsx'  # 设置您的 Excel 文件路径
df = pd.read_excel(file_path)

# 创建 MySQL 连接
connection = pymysql.connect(
    host='192.3.211.151',  # 替换为您的 MySQL 服务器地址
    user='root',           # 替换为您的用户名
    password='123456',     # 替换为您的密码
    database='FZDB',       # 使用已创建的 FZDB 数据库
    charset='utf8mb4',
    port=3307,
    autocommit=True
)

# 将数据插入到数据库
try:
    with connection.cursor() as cursor:
        # 创建 brands 表
        create_brands_table_sql = """
        CREATE TABLE IF NOT EXISTS brands (
            brand_id INT PRIMARY KEY,
            brand_name VARCHAR(255) NOT NULL
        );
        """
        cursor.execute(create_brands_table_sql)
        print('brands 表创建成功！')

        # 插入品牌数据
        # 这里使用 executemany 来批量插入
        insert_brands_sql = "INSERT INTO brands (brand_id, brand_name) VALUES (%s, %s);"
        # 将 DataFrame 格式化为适合插入的元组列表
        brands_data = list(df.itertuples(index=False, name=None))
        cursor.executemany(insert_brands_sql, brands_data)
        print('品牌数据插入成功！')

finally:
    connection.close()


'''
创建一个品牌表，我的数据在 xlsx 文件中；
表格信息如下：
ID 品牌
1 S&W 官方旗舰店
2 蕉下官方旗舰店
3 MissWiss 官方旗舰店
4 "VFU 运动旗舰店

请创建一个 FZDB 数据库将信息装入表明为,你帮我取一个
'''
