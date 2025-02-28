import pymysql

# 连接到 MySQL 服务器（注意：这里不指定数据库，因为我们要创建新的数据库）
connection = pymysql.connect(
    host='https://sql.muzihhhhhh.top',  # 替换为您的 MySQL 服务器地址
    user='root',       # 替换为您的用户名
    password='123456', # 替换为您的密码
    charset='utf8mb4',
    # port= 3307,
    autocommit=True    # 自动提交，确保对数据库的更改立即生效
)

try:
    with connection.cursor() as cursor:
        # 创建数据库的 SQL 语句
        create_db_sql = "CREATE DATABASE `muzihhh`;"
        
        # 执行创建数据库的 SQL 命令
        cursor.execute(create_db_sql)
        print('数据库创建成功！')

finally:
    # 关闭连接
    connection.close()




# CREATE TABLE IF NOT EXISTS brands_product (
#     ->         ID INT PRIMARY KEY,
#     ->         Product_Name VARCHAR(255),
#     ->         Product_Number VARCHAR(255),
#     ->         brand_id INT,
#     ->         FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE ON UPDATE CASCADE
#     -> ;


# mysql> CREATE TABLE IF NOT EXISTS brands_product (
#         ID INT AUTO_INCREMENT PRIMARY KEY,  
#         Product_Name VARCHAR(255) ,                       
#         Product_Number VARCHAR(255),              
#         brand_id INT,                              
#         FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE ON UPDATE CASCADE  
#     );

