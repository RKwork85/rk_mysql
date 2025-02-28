function main({ data1 }) {
  // 解析 JSON 字符串
  const parsedData = JSON.parse(data1);

  // 获取 'result' 数组
  const resultArray = parsedData.result;

  // 存储遍历时的结果
  const resultList = [];

  // 遍历 resultArray
  resultArray.forEach(item => {
    const { brand_id, ...itemWithoutBrandId } = item;
    resultList.push(itemWithoutBrandId);
  });

  // 创建 Markdown 表格头
  const headers = "| 产品序号 | 产品编号 | 产品名 |\n|------------|------------|--------------|";

  // 拼接表格内容
  const tableRows = resultList.map(item => {
    return `| ${item.Product_ID} |  ${item.Product_Number} |${item.Product_Name} |`;
  }).join('\n');

  // 组合成最终的 Markdown 表单字符串
  const markdownTable = `${headers}\n${tableRows}`;

  return markdownTable;
}

// 示例数据
const data = {
  data1: JSON.stringify({
    result: [
      { Product_ID: 1, Product_Number:  S4SS1067,Product_Name: '小冰纱防晒外套', brand_id: 1 },
      { Product_ID: 2, Product_Number:  S3AW1066,Product_Name: '无缝拼接鹅绒外套', brand_id: 1 }
    ]
  })
};
console.log(data)

// 执行并打印结果
console.log(main(data));