'''
对sw文案模版进行补充
 `S&W_Marketing` 
ID  int
Template text
Template_Class varchar(100)  
Template_Name varchar(255)

1. "微胖姐妹&酷盖男友速抢！
立体剪裁秒瘦5斤既视感
冰丝原纱上身自带降温buff
两位数拿下今夏最in防晒战袍
犹豫就会败北！"

2. "胯宽腿粗的宝子看过来！
H型裁剪把肉肉藏得明明白白
会呼吸的面料38°C穿也不粘身
防晒+显瘦+潮搭三合一
这波不下手真的亏！"

3. "男女同款神仙防晒衣开挂啦！
视觉抽脂术拉长全身比例
原纱材质越穿越凉快
99.9元=空调衫+防晒服+出街套装
闺蜜和男友都夸我会买系列"

4. "救命！这件防晒衣太会藏肉了！
微胖穿出纸片人既视感
男生上身秒变清爽少年感
自带清凉感的移动空调衣
现在囤三件还送冰袖！"

5. "学生党打工人的续命战衣！
H版型拯救梨形苹果型身材
透气到像没穿衣服的凉爽
99.9元搞定健身房到约会look
这价格我直接闭眼冲三件！"

6. "今夏男女通杀的王炸单品！
穿上直接PS现实身材
原纱黑科技汗不贴身
防晒指数UPF50+才两位数
刷到就是大数据在救你！"

7. "微胖界天菜防晒衣实测！
视觉减重10斤不开玩笑
百搭白/显瘦黑/元气粉三色可选
透气到能当运动内衣外穿
这性价比不囤货真的睡不着！"

8. "情侣闺蜜必入的显瘦神器！
H型剪裁拯救虎背熊腰
自带凉感的行走小空调
防晒值拉满还不到火锅钱
库存告急手慢无！"

9. "这件防晒衣让前男友后悔系列！
微胖穿出超模直角肩
男生秒变撕漫男身材
原纱面料出汗都不贴肉
现在买还送潮酷防晒面罩！"

10. "被追着问链接的显瘦玄学！
120斤穿出90斤既视感
男生套上直接去拍杂志大片
透气到能当睡衣穿的防晒衣
这个夏天错过真的会哭！"


'''
import pymysql
import json

# 数据库连接信息
connection = pymysql.connect(
    host='192.3.211.151',        # 替换为您的 MySQL 服务器地址
    user='root',                 # 替换为您的用户名
    password='123456',           # 替换为您的密码
    database='FZDB',             # 使用已创建的 FZDB 数据库
    charset='utf8mb4',
    port=3307
)

try:
    # 打开 JSON 文件并读取数据
    with open('/home/rkwork/rkwork/project/muzi_mysql/marketing_class/s&w营销2.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 创建游标对象
    with connection.cursor() as cursor:
        # 遍历 JSON 数据并插入到数据库表中
        for item in data:
            sql = """
            INSERT INTO `S&W_Marketing` (ID, Template, Template_Class, Template_Name)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (
                item['ID'],
                item['Template'],
                item['Template_Class'],
                item['Template_Name']
            ))

        # 提交事务
        connection.commit()
        print("数据插入完成！")

except Exception as e:
    print(f"发生错误：{e}")
finally:
    # 关闭数据库连接
    connection.close()