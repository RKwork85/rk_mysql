import os

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

# 列出当前目录下的所有文件
file_list= os.listdir(current_dir)
json_files = [file for file in file_list if file.endswith('.json')]

import json

dataList = []
for i in json_files:
    with open(i, 'r', encoding='utf-8') as f:
        print(f)
        data = json.load(f)
        dataList.append(data)

with open('inputCardInfo.json', 'w', encoding='utf-8') as f:
    json.dump(dataList, f, ensure_ascii=False, indent=4)