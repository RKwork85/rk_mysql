function main({ data1, userInput}) {
  // 解析 JSON 字符串
  const resultArray = JSON.parse(data1);

  // 获取 'result' 数组
    console.log(resultArray)


}

// 示例数据
const data = {
  data1: JSON.stringify(
    [
      { Product_ID: 1, Product_Number:  'S4SS1067',Product_Name: '小冰纱防晒外套', brand_id: 1 },
      { Product_ID: 2, Product_Number:  'S3AW1066',Product_Name: '无缝拼接鹅绒外套', brand_id: 1 }
    ]
  )
};
console.log(data)

// 执行并打印结果
console.log(main(data));