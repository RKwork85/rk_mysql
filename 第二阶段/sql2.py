import json
import pymysql
import os

# 定义文件路径和文件名
data_path = "/home/rkwork/rkwork/project/muzi_mysql/第二阶段/data/"
file_names = {
    "functional_videos.json": "Functional_Videos",
    "scene_videos.json": "Scene_Videos",
    "outfit_videos.json": "Outfit_Videos",
    "pain_point_videos.json": "Pain_Point_Videos"
}

# 定义模板名称前缀
prefix_map = {
    "functional_videos.json": "Ba",
    "scene_videos.json": "Bb",
    "outfit_videos.json": "Bc",
    "pain_point_videos.json": "Bd"
}

# 数据库连接函数
def fetch_db_connection():
    connection = pymysql.connect(
        host='192.3.211.151',
        user='root',
        password='123456',
        database='FZDB',
        charset='utf8mb4',
        port=3307,
        autocommit=True
    )
    return connection

# 数据填充函数
def insert_data_to_table(file_name, table_name, prefix):
    connection = fetch_db_connection()
    cursor = connection.cursor()

    # 读取JSON文件
    file_path = os.path.join(data_path, file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # 遍历JSON数据并插入到表中
    for index, item in enumerate(data, start=1):
        template_content = item.get("文案内容", "")
        template_class = item.get("话题分类", "")
        template_name = f"{prefix}{index}"

        # 插入数据
        insert_query = f"""
        INSERT INTO {table_name} (ID, Template, Template_Class, Template_Name)
        VALUES ({index}, %s, %s, %s);
        """
        cursor.execute(insert_query, (template_content, template_class, template_name))

    print(f"数据已成功插入到表 {table_name} 中！")
    cursor.close()
    connection.close()

# 主函数
def main():
    for file_name, table_name in file_names.items():
        prefix = prefix_map[file_name]
        insert_data_to_table(file_name, table_name, prefix)

# 执行主函数
if __name__ == "__main__":
    main()