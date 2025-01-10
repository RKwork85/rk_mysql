'''
我需要修改 id 为4 的数据将为 VFU 运动旗舰店
'''
import pymysql

def update_brand():
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
            # 更新数据
            update_query = "UPDATE brands SET brand_name = 'VFU运动旗舰店' WHERE brand_id = 4"
            cursor.execute(update_query)
            # 提交更改
            connection.commit()

    finally:
        connection.close()

if __name__ == '__main__':
    update_brand()