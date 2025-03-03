# import pymysql

# def create_table():
#     connection = pymysql.connect(
#         host='192.3.211.151',  # 替换为您的 MySQL 服务器地址
#         user='root',  # 替换为您的用户名
#         password='123456',  # 替换为您的密码
#         database='FZDB',  # 使用 FZDB 数据库
#         charset='utf8mb4',
#         port=3307,
#         autocommit=True
#     )
    
#     try:
#         with connection.cursor() as cursor:
#             sql = """
#             CREATE TABLE IF NOT EXISTS Prompt_Template (
#                 ID INT AUTO_INCREMENT PRIMARY KEY,
#                 Prompt TEXT NOT NULL,
#                 Prompt_Class VARCHAR(255) NOT NULL,
#                 Template_Table VARCHAR(255) NOT NULL
#             );
#             """
#             cursor.execute(sql)
#             print("表创建成功！")
#     finally:
#         connection.close()

# # 调用函数
# create_table()



import pymysql

# 数据库连接函数
def create_connection():
    connection = pymysql.connect(
        host='192.3.211.151',  # 数据库地址
        user='root',           # 用户名
        password='123456',     # 密码
        database='FZDB',       # 数据库名称
        charset='utf8mb4',     # 字符集
        port=3307,             # 端口
        autocommit=True        # 自动提交
    )
    return connection

# 创建表
def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    
    # 创建表的SQL语句
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS Prompt_Template (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Prompt TEXT NOT NULL,
        Prompt_Class VARCHAR(255) NOT NULL
    );
    """
    cursor.execute(create_table_sql)
    print("表 Prompt_Template 创建成功！")
    cursor.close()
    connection.close()

# 插入数据
def insert_data():
    connection = create_connection()
    cursor = connection.cursor()
    
    # 数据一
    prompt1 = """
    请参考文案模版的行文逻辑，将输入的产品信息经过处理后，融入模版中，生成一篇文案内容，语言要精美，能够抓住用户的心理。
    文案要求：
    1、工作逻辑要求：分析文案模板中第一句话的产品的特性是什么，然后在生成的文案中的第一句话也要围绕着这个特性生成文案。
    3、生成的文案的字数要求：生成的文案内容不超过150字
    4、生成文案的数量要求：2篇
    5、输出文案的格式要求：
    {"文案一":"文案内容","文案二":"文案内容"}
    
    文案模版如下：

    """
    prompt_class1 = "Functional_Videos_Marketing"

    # 数据二
    prompt2 = """
    请从输入的产品属性中选择一条卖点，仿照文案模版进行文案创作，
    文案要求：
    1、生成的文案内容尽量为产品本身的通用属性，比如：好看，百搭，显瘦的角度去说明。
    2、细节方面只选择产品属性中的一条。
    3、输出的字数和文案模版长度类似，
    4、生成文案的数量要求：2篇
    5、输出文案的格式要求：
    {"文案一":"文案内容","文案二":"文案内容"}
    
    文案模版如下：

    """
    prompt_class2 = "Functional_Videos_Marketing"
    Template_Table1 = "Functional_Videos_Marketing"
    Template_Table2 = "S&W_Marketing"

    # 插入数据的SQL语句
    insert_sql = "INSERT INTO Prompt_Template (Prompt, Prompt_Class, Template_Table) VALUES (%s, %s, %s)"
    
    # 插入数据
    cursor.execute(insert_sql, (prompt1, prompt_class1, Template_Table1))
    cursor.execute(insert_sql, (prompt2, prompt_class2, Template_Table2))
    
    print("数据插入成功！")
    cursor.close()
    connection.close()

# 主函数
if __name__ == "__main__":
    create_table()  # 创建表
    insert_data()   # 插入数据