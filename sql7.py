'''
链接数据库查找所有表数据；我需要查找这张表的数据和字段
'''
import pymysql

def fetch_all_brands():
    # 创建 MySQL 连接
    connection = pymysql.connect(
        host='192.3.211.151',  # 替换为您的 MySQL 服务器地址
        user='root',  # 替换为您的用户名
        password='123456',  # 替换为您的密码
        database='FZDB',  # 使用 FZDB 数据库
        charset='utf8mb4',
        port=3307,
        autocommit=True
    )

    try:
        with connection.cursor() as cursor:
            # 查询所有品牌数据
            cursor.execute("SELECT * FROM brands")
            brands = cursor.fetchall()

            # 打印字段信息
            field_names = [i[0] for i in cursor.description]
            print("字段信息：", field_names)

            # 打印每条记录
            for brand in brands:
                print(brand)

    finally:
        connection.close()

if __name__ == '__main__':
    fetch_all_brands()