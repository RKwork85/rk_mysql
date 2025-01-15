## Pymysql 操作 Myslq8 数据库

## 背景说明

>动力都是被逼出来的，生活逼出来的，工作逼出来的。

- 这不是一件坏事


数据库语言：


 1、查询某表某列等于某值的 特定数据
```
要查询 brands_product 表中 brand_id 列等于 1的所有数据，你可以使用 SQL 的 SELECT 语句。以下是一个示例查询：

SELECT * FROM brands_product WHERE brand_id = 1;
这个查询将返回 brands_product 表中所有 brand_id 等于 1的记录。如果你只需要特定的列，可以在 SELECT 后面指定列名，例如：

SELECT column1, column2 FROM brands_product WHERE brand_id = 1;


ALTER TABLE brands_product
ADD COLUMN Product_Number VARCHAR(255) AFTER Product_ID;
AFTER Product_ID: 这个部分指定了将 Product_Number 列添加到 Product_ID 列之后。

选择 品牌账号对应的品牌名称
SELECT nick_name FROM brands WHERE brand_name ='{{$VARIABLE_NODE_ID.品牌$}}'


bug:返回的字段全都是第一个表的字段

SELECT * FROM Product_FabDescription WHERE Card = 1
UNION ALL
SELECT * FROM Product_FabricTagline WHERE Card = 1
UNION ALL
SELECT * FROM Product_Process WHERE Card = 1
UNION ALL
SELECT * FROM Product_SportScenes WHERE Card = 1
UNION ALL
SELECT * FROM Product_Tagline WHERE Card = 1
UNION ALL
SELECT * FROM Product_UserPainPoints WHERE Card = 1
UNION ALL
SELECT * FROM Product_patternTagline WHERE Card = 1
UNION ALL
SELECT * FROM Product_Color WHERE Card = 1
UNION ALL
SELECT * FROM Product_DesignTagline WHERE Card = 1;
UNION ALL
SELECT * FROM Product_FabricDescription WHERE Card = 1;
```

2、查询某表的外键关系

```
SELECT 
    TABLE_NAME, 
    CONSTRAINT_NAME 
FROM 
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE 
WHERE 
    REFERENCED_TABLE_NAME = 'brands_product' 
    AND TABLE_SCHEMA = 'FZDB';


删除某表的外键关系名

ALTER TABLE table_name DROP FOREIGN KEY constraint_name;
+---------------------------+----------------------------------+
| TABLE_NAME                | CONSTRAINT_NAME                  |
+---------------------------+----------------------------------+
| Product_Color             | Product_Color_ibfk_1             |
| Product_DesignTagline     | Product_DesignTagline_ibfk_1     |
| Product_FabDescription    | Product_FabDescription_ibfk_1    |
| Product_FabricDescription | Product_FabricDescription_ibfk_1 |
| Product_FabricTagline     | Product_FabricTagline_ibfk_1     |
| Product_Process           | Product_Process_ibfk_1           |
| Product_SportScenes       | Product_SportScenes_ibfk_1       |
| Product_Tagline           | Product_Tagline_ibfk_1           |
| Product_UserPainPoints    | Product_UserPainPoints_ibfk_1    |
| Product_patternTagline    | Product_patternTagline_ibfk_1    |
如上

删除外键约束：
ALTER TABLE Product_Color DROP FOREIGN KEY Product_Color_ibfk_1;

```

3、数据库备份
```
mysqldump -u 用户名 -p 数据库名 > 备份文件.sql
如果要备份所有的数据库，可以使用：

mysqldump -u 用户名 -p --all-databases > 备份文件.sql
备份多个数据库，可以使用 --databases 参数：

mysqldump -u 用户名 -p --databases 数据库名 1 数据库名 2 > 备份文件.sql

```

4、查找一个表的表结构
```

 
```

<!-- "429 当前分组上游负载已饱和，请稍后再试 (request id: 2025011602522429843161948780139)", -->