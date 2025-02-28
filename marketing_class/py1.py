import csv

def read_and_process_file(input_file, output_file):
    # 打开输入文件并读取所有行
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 去除每行的换行符并过滤空行
    lines = [line.strip() for line in lines if line.strip()]

    # 初始化表格数据
    table_data = []
    product_id = "S4SS1067"
    template_id = "Bh11"

    # 按每五行分组处理
    for i in range(0, len(lines), 5):
        for j in range(5):
            if i + j < len(lines):  # 确保不超出列表范围
                table_data.append([product_id, template_id, lines[i + j]])
        template_id = f"Bh{int(template_id[2:]) + 1:02d}"  # 更新模板编号

    # 将结果保存到CSV文件
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["产品编号", "模板编号", "文案内容"])  # 写入表头
        writer.writerows(table_data)  # 写入数据

    print(f"处理完成，结果已保存到 {output_file}")

# 调用函数
input_file = "/home/rkwork/rkwork/project/muzi_mysql/marketing_class/data.txt"  # 输入文件名
output_file = "output.csv"  # 输出文件名
read_and_process_file(input_file, output_file)