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
    return connection

def create_tables():
    connection = fetch_all_brands()
    cursor = connection.cursor()

    # 定义表的创建语句
    create_functional_videos = """
    CREATE TABLE IF NOT EXISTS Functional_Videos_Explanation (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Template TEXT,
        Template_Class VARCHAR(100),
        Template_Name VARCHAR(255)
    );
    """
    create_scene_videos = """
    CREATE TABLE IF NOT EXISTS Scene_Videos_Explanation (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Template TEXT,
        Template_Class VARCHAR(100),
        Template_Name VARCHAR(255)
    );
    """
    create_outfit_videos = """
    CREATE TABLE IF NOT EXISTS Outfit_Videos_Explanation (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Template TEXT,
        Template_Class VARCHAR(100),
        Template_Name VARCHAR(255)
    );
    """
    create_pain_point_videos = """
    CREATE TABLE IF NOT EXISTS Pain_Point_Videos_Explanation (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Template TEXT,
        Template_Class VARCHAR(100),
        Template_Name VARCHAR(255)
    );
    """

    # 执行表创建语句
    cursor.execute(create_functional_videos)
    cursor.execute(create_scene_videos)
    cursor.execute(create_outfit_videos)
    cursor.execute(create_pain_point_videos)

    print("所有表已成功创建！")
    cursor.close()
    connection.close()

# 调用函数创建表
create_tables()