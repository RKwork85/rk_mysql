import multiprocessing
import os
import json 
import time
from openai import OpenAI
import re
question_data='''
产品名：宽下摆运动内衣
货号：S3SS8529
颜色：明月白、樱草黄、深邃黑、焦糖棕、珊瑚粉、摩卡棕、烟灰蓝、丝绒红
工艺：净色
用户痛点：
1. 希望找到一款能够有效隐藏副乳的运动内衣。
2. 想要一款穿着舒适，不勒腰的运动内衣。
3. 期望运动内衣具有良好的支撑和收束效果，能展现好身材。
4. 希望运动内衣的散热性能好，穿着清爽。
5. 想要一款外穿时不会感到尴尬的运动内衣。
运动场景：器械、跑步、跳绳、骑行
FAB 产品解说：
1. 侧翼加高。隐藏副乳，贴合身体。使穿着者视觉上更显瘦，增强自信心。
2. 加宽下摆。舒适不勒腰。提供良好的穿着体验，减少束缚感。
3. 丝滑弹力面料。支撑胸部，收束赘肉。帮助塑造好身材，展现女性魅力。
4. V形美背。提升散热能力，大方露出背部肌肤。让穿着者在运动中保持清爽，同时展现出迷人的背部曲线。
面料解说：
1. 面料成分包含75%锦纶和25%氨纶，具有良好的弹性和延展性。
2. 锦纶和氨纶的组合，使面料具有吸湿排汗功能，保持身体干爽。
3. 丝滑的面料质感，提供舒适的肌肤触感。
4. 面料的弹力性能，使得运动内衣能够更好地贴合身体，提供良好的支撑。
一句话宣传：外穿无压力的运动内衣，超适合夏天户外！
面料宣传：
1. 优质面料，吸湿排汗，让您时刻保持干爽舒适。
2. 丝滑弹力面料，舒适支撑，展现完美身姿。
版型宣传：贴合身形的设计，提供舒适的穿着体验。
设计宣传：
1. 加长背心式设计，外穿自信不尴尬。
2. V形美背设计，凸显迷人曲线。
3. 侧翼加高设计，有效隐藏副乳。
4. 加宽下摆设计，舒适无束缚。



'''
import os

def get_json_file_count():
    """
    获取当前目录下所有 JSON 文件名列表，并返回从最新 JSON 文件名中提取的数字加一到 50 之间的范围列表。
    
    :return: 一个包含范围的列表。
    """
    # 切换到当前文件所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)

    # 列出当前目录下的所有文件
    file_list = os.listdir(current_dir)

    # 创建一个包含所有 JSON 文件名的列表
    json_file_names = [file for file in file_list if file.endswith('.json')]

    # 升序排列 JSON 文件名列表
    json_file_names_sorted = sorted(json_file_names)

    # 检查是否有 JSON 文件
    if json_file_names_sorted:
        print("JSON 文件名列表:", json_file_names_sorted)  # 打印文件名列表为调试
        # 获取最新文件名并提取相应的数字
        latest_json_file = json_file_names_sorted[-1]
        extracted_number = int(latest_json_file[4])  # 根据需求获取指定索引的字符
        
        # 生成范围列表
        count = [number for number in range(extracted_number + 1, 50)]
        return count
    else:
        print("当前目录没有 JSON 文件。")
        return []

# 调用函数并获取结果
result = get_json_file_count()
print("生成的计数范围:", result)

def chat_request(question):
    # 在函数内部创建client实例
    client = OpenAI(
       base_url="http://aiagent-pre.chengwen.net/api/v1",  
       api_key="prechengwenai-sLn3UjeZcwTFplnsfGHKkbGKQ119eiBvuOccEUYFPhPIrrQYzYQO4AQaeMH"
    )


    try:    #整个程序的try
        completion = client.chat.completions.create(
            model="doubao-pro-128k",
            messages=[{'role': 'user', 'content': f'{question}'}],
        )
        
        completion_cp = completion.model_dump_json()
        data = json.loads(completion_cp)
        content = (data["choices"][0]['message']['content'])

        json_pattern = r'```json\n(.*?)```'
        json_match = re.search(json_pattern, content, re.DOTALL)
        if json_match:
            str_data = json_match.group(1)
            
            try:        # openai数据格式返回的try
                 json_data = json.loads(str_data)

                 return json_data
            except:
                return 1
        else:           # 豆包数据格式返回的try
            try:
                json.loads(content)
                return 0  
            except:
                return 1
    except Exception as e:
        return 1  



start = time.time()

import os
import json

# 获取当前工作目录
current_dir = os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 列出当前目录下的所有文件
file_list = os.listdir(current_dir)

# 创建一个包含所有 JSON 文件名的列表
json_file_names = [file for file in file_list if file.endswith('.json')]

json_file_names_sorted = sorted(json_file_names)

# 打印升序排列的 JSON 文件名列表
print(json_file_names_sorted[-1][4])


count = [number for number in range(int(json_file_names_sorted[-1][4])+1, 50)]
print(count)



print(count)
task = [question_data for _ in range(1) ]
with multiprocessing.Pool(processes=20) as pool:
    results = pool.map_async(chat_request, task)

    for index,result in enumerate(results.get()):
        print(result)
        count = get_json_file_count()
        file_name = "json" + str(count[0]) +'.json'
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
            f.flush()
        

end = time.time()
print('count:', count)
print(f"最终执行时间{end - start}")