import pymysql

# 连接到 MySQL 服务器（注意：这里不指定数据库，因为我们要创建新的数据库）
connection = pymysql.connect(
    host='192.3.211.151',  # 替换为您的 MySQL 服务器地址
    user='root',           # 替换为您的用户名
    password='123456',     # 替换为您的密码
    charset='utf8mb4',
    port=3307,
    autocommit=True        # 自动提交，确保对数据库的更改立即生效
)

try:
    with connection.cursor() as cursor:
        # 创建数据库的 SQL 语句
        create_db_sql = "CREATE DATABASE IF NOT EXISTS `FZDB`;"
        
        # 执行创建数据库的 SQL 命令
        cursor.execute(create_db_sql)
        print('数据库创建成功！')

finally:
    # 关闭连接
    connection.close()

# 再次连接到刚刚创建的数据库 FZDB
connection = pymysql.connect(
    host='192.3.211.151',
    user='root',
    password='123456',
    database='FZDB',  # 连接到 FZDB 数据库
    charset='utf8mb4',
    port=3307,
    autocommit=True
)

try:
    with connection.cursor() as cursor:
        # 创建 users 表
        create_users_table_sql = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
        """
        cursor.execute(create_users_table_sql)
        print('users 表创建成功！')
        
        # 创建 orders 表
        create_orders_table_sql = """
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            order_date DATE NOT NULL,
            user_id INT,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
        """
        cursor.execute(create_orders_table_sql)
        print('orders 表创建成功！')

        # 插入示例数据到 users 表
        insert_users_sql = "INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie');"
        cursor.execute(insert_users_sql)
        
        # 插入示例数据到 orders 表
        insert_orders_sql = """
        INSERT INTO orders (order_date, user_id) VALUES 
        ('2023-10-01', 1), 
        ('2023-10-02', 2), 
        ('2023-10-03', 1);
        """
        cursor.execute(insert_orders_sql)
        
        # 查询所有订单及其关联的用户信息
        select_sql = """
        SELECT 
            orders.order_id, 
            orders.order_date, 
            users.name AS user_name
        FROM 
            orders
        JOIN 
            users ON orders.user_id = users.user_id;
        """
        cursor.execute(select_sql)
        results = cursor.fetchall()
        
        for row in results:
            print(f"Order ID: {row[0]}, Order Date: {row[1]}, User Name: {row[2]}")

finally:
    # 关闭连接
    connection.close()