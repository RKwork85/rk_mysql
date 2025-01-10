import pandas as pd
import pymysql
import os

def get_brand_id(cursor, brand_name):
    cursor.execute("SELECT brand_id FROM brands WHERE brand_name = %s", (brand_name,))
    result = cursor.fetchone()
    return result[0] if result else None

def read_and_clean_excel(file):
    df = pd.read_excel(file)
    # 处理 NaN 值
    return df.where(pd.notnull(df), None)

def insert_data(cursor, data, brand_id):
    insert_sql = """
    INSERT INTO douyin_target_accounts (
        blogger, url, awesome_id, title, comment_count, share_count,
        like_count, favorite_count, video_publish_time, collect_time, brand_id
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    data_to_insert = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], brand_id) 
                      for row in data.itertuples(index=False, name=None)]
    cursor.executemany(insert_sql, data_to_insert)

def main():
    connection = pymysql.connect(
        host='192.3.211.151',
        user='root',
        password='123456',
        database='FZDB',
        charset='utf8mb4',
        port=3307,
        autocommit=True
    )
    
    files = [
        # '蕉下官方旗舰店.xlsx', 
        # 'MissWiss官方旗舰店.xlsx', 
        # 'S&W官方旗舰店.xlsx', 
        'VFU运动旗舰店.xlsx'
    ]

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS douyin_target_accounts (
                    blogger VARCHAR(255),
                    url VARCHAR(500),
                    awesome_id VARCHAR(255),
                    title TEXT,
                    comment_count INT,
                    share_count INT,
                    like_count INT,
                    favorite_count INT,
                    video_publish_time DATETIME,
                    collect_time DATETIME,
                    brand_id INT,
                    FOREIGN KEY (brand_id) REFERENCES brands(brand_id)
                );
            """)
            print('douyin_target_accounts 表创建成功！')

            for file in files:
                df = read_and_clean_excel(file)
                brand_name = os.path.splitext(file)[0]
                print(brand_name)
                brand_id = get_brand_id(cursor, brand_name)
                print(brand_id)
                if brand_id:
                    insert_data(cursor, df, brand_id)
                    print(f'{file} 的数据插入成功！')
                else:
                    print(f'{file} 找不到对应的品牌 ID 。')

    finally:
        connection.close()

if __name__ == '__main__':
    main()