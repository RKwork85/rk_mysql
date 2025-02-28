import pymysql

# 创建数据库连接
connection = pymysql.connect(
    host='192.3.211.151',
    user='root',
    password='123456',
    database='FZDB',
    charset='utf8mb4',
    port=3307
)

try:
    with connection.cursor() as cursor:
        # SQL 查询
        sql_query = """
        SELECT bp.*,
               pc.*,
               pfd.*,
               pft.*,
               pp.*,
               pss.*,
               pt.*,
               pup.*,
               ppt.*
        FROM brands_product bp
        LEFT JOIN Product_Color pc ON bp.Product_ID = pc.Card
        LEFT JOIN Product_FabDescription pfd ON bp.Product_ID = pfd.Card
        LEFT JOIN Product_FabricTagline pft ON bp.Product_ID = pft.Card
        LEFT JOIN Product_Process pp ON bp.Product_ID = pp.Card
        LEFT JOIN Product_SportScenes pss ON bp.Product_ID = pss.Card
        LEFT JOIN Product_Tagline pt ON bp.Product_ID = pt.Card
        LEFT JOIN Product_UserPainPoints pup ON bp.Product_ID = pup.Card
        LEFT JOIN Product_patternTagline ppt ON bp.Product_ID = ppt.Card
        WHERE bp.Product_ID = 1;
        """
        
        # 执行 SQL 查询
        cursor.execute(sql_query)
        results = cursor.fetchall()

        # 输出结果
        for row in results:
            print(row)

finally:
    connection.close()