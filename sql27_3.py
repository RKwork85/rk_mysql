'''
实现卡片信息的批量化存储

'''

import pymysql
dataJson = {
    "产品名": ["夹克外套"],
    "产品编号": ["S4AW1239"],
    "颜色": ["森林绿", "火山灰", "曜石黑", "暗夜红"],
    "工艺": ["净色"],
    "用户痛点": [
      "期望找到一件既具有复古美感又具备强大功能性的外套。",
      "担心外套的防风、防水效果不佳。",
      "希望外套穿着舒适，不闷热。",
      "想要一件能够修饰身材的外套。"
    ],
    "运动场景": ["日常", "休闲", "户外", "通勤"],
    "FAB 产品解说": [
      "防风防泼水外套。有效抵御风雨，保持身体干爽。让您在户外活动或通勤时无需担心天气变化。",
      "可调节防风帽。根据需要灵活调整，防风挡雨且不遮挡视野。提供更好的防护，同时不影响视线，增加安全性和便利性。",
      "插肩设计。修饰肩部线条。使您看起来更显瘦，背部显得更薄，提升整体美观度。",
      "腋下撞色透气孔。加速散热，保持身体干爽。让您在穿着时不会感到闷热，提高舒适度。"
    ],
    "面料解说": [
      "面料采用 100%锦纶，具有良好的耐磨性。",
      "高品质防风防泼水面料，有效阻挡风雨。",
      "面料挺阔有型，使外套上身更显质感。",
      "锦纶面料的使用，让外套具有较好的耐用性。"
    ],
    "一句话宣传": ["出街小夹克，简单又耐看！"],
    "面料宣传": [
      "精选 100%锦纶面料，防风防水，伴您无畏风雨。",
      "高品质锦纶面料，耐磨挺阔，彰显非凡质感。"
    ],
    "版型宣传": ["宽松版型，穿着舒适自在，无束缚感。"],
    "设计宣传": [
      "都市休闲风设计，展现时尚魅力，轻松驾驭各种场合。",
      "可调节防风帽设计，贴心防护，适应不同天气需求。",
      "两侧斜插袋设计，方便实用，满足您的日常需求。",
      "插肩设计，修饰身形，让您更加自信美丽。"
    ]
  }

# 数据库连接
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
        # 查询当前记录数量
        cursor.execute("SELECT COUNT(*) FROM brands_product")
        result = cursor.fetchone()  # 获取结果
        current_count = result[0] if result else 0

        # 下一个 Product_ID 为当前记录数量+1
        next_product_id = current_count + 1
        CardId = next_product_id
        print(next_product_id)
        # SQL 插入语句

        # 实现产品名
        sql_cardInfo = """
        INSERT INTO brands_product (Product_ID,Product_Number, Product_Name, brand_id)
        VALUES (%s,%s, %s, %s)
        """
        data = ( next_product_id, dataJson['产品编号'], dataJson['产品名'], 1)
        cursor.execute(sql_cardInfo, data)

        # # 增加颜色
        cursor.execute("SELECT COUNT(*) FROM Product_Color")
        result = cursor.fetchone()[0]
        print(result)
        insertColor = """
        INSERT INTO Product_Color(ID, Product_Color, Tag, Card)
        VALUES(%s, %s, %s, %s)
        """
        for index, i in enumerate(dataJson['颜色']):
          data = (index+1+result,  i, "颜色", CardId ) 
          cursor.execute(insertColor, data)   

        ## 增加设计宣传
        cursor.execute("SELECT COUNT(*)FROM Product_DesignTagline ")
        count = cursor.fetchone()[0]

        inserDesignTagline='''
        Insert INTO Product_DesignTagline(ID, Product_DesignTagline, Tag, Card)
        Values(%s, %s, %s, %s)
'''
        for index, i in enumerate(dataJson['设计宣传']):
            data= (index + 1 + count, i, "设计宣传", CardId)
            cursor.execute(inserDesignTagline, data)

        ## 增加FAB解说
        cursor.execute("SELECT COUNT(*)FROM Product_FabDescription ")
        count = cursor.fetchone()[0]

        inserDesignTagline='''
        Insert INTO Product_FabDescription(ID, Product_FabDescription, Tag, Card)
        Values(%s, %s, %s, %s)
'''
        for index, i in enumerate(dataJson['FAB 产品解说']):
            data= (index + 1 + count, i, "FAB 产品解说", CardId)
            cursor.execute(inserDesignTagline, data)
        


        ## 增加面料解说
        cursor.execute("SELECT COUNT(*)FROM Product_FabricDescription ")
        count = cursor.fetchone()[0]

        inserDesignTagline='''
        Insert INTO Product_FabricDescription(ID, Product_FabricDescription, Tag, Card)
        Values(%s, %s, %s, %s)
'''
        for index, i in enumerate(dataJson['面料解说']):
            data= (index + 1 + count, i, "面料解说", CardId)
            cursor.execute(inserDesignTagline, data)

        ## 增加面料宣传
        cursor.execute("SELECT COUNT(*)FROM Product_FabricTagline ")
        count = cursor.fetchone()[0]

        inserDesignTagline='''
        Insert INTO Product_FabricTagline(ID, Product_FabricTagline, Tag, Card)
        Values(%s, %s, %s, %s)
'''
        for index, i in enumerate(dataJson['面料宣传']):
            data= (index + 1 + count, i, "面料宣传", CardId)
            cursor.execute(inserDesignTagline, data)



        ## 增加产品工艺
        cursor.execute("SELECT COUNT(*)FROM Product_Process ")
        count = cursor.fetchone()[0]

        inserDesignTagline='''
        Insert INTO Product_Process(ID, Product_Process, Tag, Card)
        Values(%s, %s, %s, %s)
'''
        for index, i in enumerate(dataJson['工艺']):
            data= (index + 1 + count, i, "工艺", CardId)
            cursor.execute(inserDesignTagline, data)

        ## 增加运动场景
        cursor.execute("SELECT COUNT(*)FROM Product_SportScenes ")
        count = cursor.fetchone()[0]

        inserDesignTagline='''
        Insert INTO Product_SportScenes(ID, Product_SportScenes, Tag, Card)
        Values(%s, %s, %s, %s)
'''
        for index, i in enumerate(dataJson['运动场景']):
            data= (index + 1 + count, i, "运动场景", CardId)
            cursor.execute(inserDesignTagline, data)

        ## 增加宣传语
        cursor.execute("SELECT COUNT(*)FROM Product_Tagline ")
        count = cursor.fetchone()[0]

        inserDesignTagline='''
        Insert INTO Product_Tagline(ID, Product_Tagline, Tag, Card)
        Values(%s, %s, %s, %s)
'''
        for index, i in enumerate(dataJson['一句话宣传']):
            data= (index + 1 + count, i, "一句话宣传", CardId)
            cursor.execute(inserDesignTagline, data)


        ## 增加用户痛点
        cursor.execute("SELECT COUNT(*)FROM Product_UserPainPoints ")
        count = cursor.fetchone()[0]

        inserDesignTagline='''
        Insert INTO Product_UserPainPoints(ID, Product_UserPainPoints, Tag, Card)
        Values(%s, %s, %s, %s)
'''
        for index, i in enumerate(dataJson['用户痛点']):
            data= (index + 1 + count, i, "用户痛点", CardId)
            cursor.execute(inserDesignTagline, data)
        
        
        ## 版型宣传 
        cursor.execute("SELECT COUNT(*)FROM Product_PatternTagline ")
        count = cursor.fetchone()[0]

        inserDesignTagline='''
        Insert INTO Product_PatternTagline(ID, Product_PatternTagline, Tag, Card)
        Values(%s, %s, %s, %s)
'''
        for index, i in enumerate(dataJson['版型宣传']):
            data= (index + 1 + count, i, "版型宣传", CardId)
            cursor.execute(inserDesignTagline, data)
        
        
        



        
        # INSERT INTO Product_Color (ID, Product_Color, Tag, Card)
        # VALUES (%s, %s, %s, %s)

        # data = (next_product_id, dataJson['产品编号'], dataJson['产品名'], next_product_id)
        # cursor.execute(sql_cardInfo, data)
        # """
        # for item in data:
        #   cursor.execute(insertColor, (item['颜色'], '颜色', next_product_id))  # 为 tag 字段赋值为'颜色'
        
        # 执行 SQL，并传入数据
        connection.commit()  # 提交事务

        print("数据插入成功! Product_ID 为:", next_product_id)

finally:
    connection.close()  # 确保关闭连接