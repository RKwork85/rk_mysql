# 我需要查找 douyin_target_accounts 中 按 video_publish_time 和 brand_id 为 2 的最新的前十条数据
import pymysql

def fetch_latest_data():
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
            # 查询满足条件的最新的前十条数据
            query = """
            SELECT * 
            FROM douyin_target_accounts 
            WHERE brand_id = 2 
            ORDER BY video_publish_time DESC       
            LIMIT 10
            """                     #: 按照video_publish_time字段降序排列（即最新的排在前面）
            cursor.execute(query)
            results = cursor.fetchall()

            for result in results:
                print(result)
    finally:
        connection.close()

if __name__ == '__main__':
    fetch_latest_data()