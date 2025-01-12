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
    with connection.cursor() as cursor:
        # 查询 brand_name 为 'S&W 官方旗舰店' 的 nick_name
        query = "SELECT `nick_name` FROM `brands` WHERE `brand_name` = %s"
        cursor.execute(query, ('S&W官方旗舰店',))
        
        # 获取查询结果
        result = cursor.fetchone()  # 获取一条结果
        
        if result:
            print(f"品牌 'S&W官方旗舰店' 的昵称是: {result[0]}")
        else:
            print("没有找到品牌 'S&W官方旗舰店' 的记录。")
finally:
    connection.close()