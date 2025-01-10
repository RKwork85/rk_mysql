'''
修改表名字
'''
import pymysql

def modify_table_structure():
    # 创建 MySQL 连接
    connection = pymysql.connect(
        host='192.3.211.151',  
        user='root',  
        password='123456',  
        database='FZDB',  
        charset='utf8mb4',
        port=3307
    )

    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 修改表结构的 SQL 语句
        alter_table_query = """
        ALTER TABLE brands_product
        CHANGE ID Product_ID INT,
        CHANGE 产品名 Product_Name VARCHAR(255)
        """

        # 执行修改表结构的语句
        cursor.execute(alter_table_query)

        # 提交更改
        connection.commit()

    except pymysql.Error as e:
        # 发生错误时回滚
        connection.rollback()
        print(f"修改表结构时发生错误: {e}")

    finally:
        # 关闭游标和连接
        cursor.close()
        connection.close()

if __name__ == "__main__":
    modify_table_structure()